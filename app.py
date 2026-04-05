from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime
from collections import defaultdict
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
DATA_FILE = 'data/water_data.json'

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/api/submit', methods=['POST'])
def submit_data():
    data = request.json
    prev_level = float(data['prevLevel'])
    curr_level = float(data['currLevel'])
    water_used = prev_level - curr_level
    
    entry = {
        'date': data['date'],
        'time': data['time'],
        'tankCapacity': float(data['tankCapacity']),
        'prevLevel': prev_level,
        'currLevel': curr_level,
        'waterUsed': water_used,
        'students': int(data['students']),
        'area': data['area'],
        'block': data['block'],
        'timestamp': datetime.now().isoformat()
    }
    
    all_data = load_data()
    all_data.append(entry)
    save_data(all_data)
    
    return jsonify({'success': True, 'waterUsed': water_used})

@app.route('/api/analytics')
def analytics():
    data = load_data()
    if not data:
        return jsonify({'error': 'No data available'})
    
    # Filter by date if provided
    filter_date = request.args.get('date')
    if filter_date:
        data = [d for d in data if d['date'] == filter_date]
        if not data:
            return jsonify({'error': f'No data available for {filter_date}'})
    
    total_usage = sum(d['waterUsed'] for d in data)
    total_students = sum(d['students'] for d in data)
    avg_per_student = total_usage / total_students if total_students > 0 else 0
    
    # Peak usage time
    time_usage = defaultdict(float)
    for d in data:
        hour = d['time'].split(':')[0]
        time_usage[hour] += d['waterUsed']
    peak_time = max(time_usage.items(), key=lambda x: x[1])[0] if time_usage else '00'
    
    # Usage by area
    area_usage = defaultdict(float)
    for d in data:
        area_usage[d['area']] += d['waterUsed']
    
    # Daily usage
    daily_usage = defaultdict(float)
    for d in data:
        daily_usage[d['date']] += d['waterUsed']
    
    # Time series data
    time_series = [{'time': d['time'], 'usage': d['waterUsed'], 'date': d['date']} for d in data]
    
    # Abnormal usage detection
    avg_usage = total_usage / len(data)
    abnormal = any(d['waterUsed'] > avg_usage * 1.4 for d in data)
    abnormal_entries = [{'time': d['time'], 'date': d['date'], 'usage': d['waterUsed']} 
                        for d in data if d['waterUsed'] > avg_usage * 1.4]
    
    # Hourly usage for heatmap
    hourly_usage = defaultdict(float)
    hourly_count = defaultdict(int)
    for d in data:
        hour = int(d['time'].split(':')[0])
        hourly_usage[hour] += d['waterUsed']
        hourly_count[hour] += 1
    
    # Heatmap data
    heatmap_data = []
    for hour in range(24):
        avg_hour_usage = hourly_usage[hour] / hourly_count[hour] if hourly_count[hour] > 0 else 0
        heatmap_data.append({'hour': hour, 'usage': round(avg_hour_usage, 2)})
    
    # Water Efficiency Score
    expected_usage_per_student = 120  # liters per day
    unique_students = len(set(d['students'] for d in data))
    total_days = len(set(d['date'] for d in data))
    expected_total = expected_usage_per_student * (total_students / len(data)) * total_days
    efficiency_score = min(100, (expected_total / total_usage * 100)) if total_usage > 0 else 0
    
    if efficiency_score >= 90:
        efficiency_category = 'Excellent'
    elif efficiency_score >= 70:
        efficiency_category = 'Moderate'
    else:
        efficiency_category = 'Poor'
    
    # Per Student Water Footprint
    per_student_daily = avg_per_student / len(data) if len(data) > 0 else 0
    
    # Tank Refill Prediction
    latest_entry = data[-1] if data else None
    tank_refill_hours = None
    if latest_entry and len(data) > 1:
        recent_data = data[-5:] if len(data) >= 5 else data
        avg_hourly_consumption = sum(d['waterUsed'] for d in recent_data) / len(recent_data)
        remaining_water = latest_entry['currLevel']
        if avg_hourly_consumption > 0:
            tank_refill_hours = round(remaining_water / avg_hourly_consumption, 2)
    
    # Weekly usage
    weekly_usage = sum(daily_usage.values()) if len(daily_usage) <= 7 else sum(list(daily_usage.values())[-7:])
    
    # Water saved compared to previous day
    water_saved = 0
    if len(daily_usage) >= 2:
        sorted_dates = sorted(daily_usage.keys())
        today_usage = daily_usage[sorted_dates[-1]]
        yesterday_usage = daily_usage[sorted_dates[-2]]
        water_saved = yesterday_usage - today_usage
    
    # Dynamic Conservation suggestions
    suggestions = []
    
    # Time-based analysis
    morning_usage = sum(d['waterUsed'] for d in data if 6 <= int(d['time'].split(':')[0]) <= 9)
    evening_usage = sum(d['waterUsed'] for d in data if 18 <= int(d['time'].split(':')[0]) <= 21)
    night_usage = sum(d['waterUsed'] for d in data if 22 <= int(d['time'].split(':')[0]) or int(d['time'].split(':')[0]) <= 5)
    
    if morning_usage > total_usage * 0.4:
        suggestions.append(f"Morning usage is {round(morning_usage/total_usage*100)}% of total. Stagger bathing schedules between 6-9 AM.")
    
    if evening_usage > total_usage * 0.35:
        suggestions.append(f"Evening peak detected ({round(evening_usage)} L). Distribute activities across different times.")
    
    if night_usage > total_usage * 0.15:
        suggestions.append(f"High night usage detected ({round(night_usage)} L). Check for leaks or unauthorized usage.")
    
    # Area-based analysis
    bathroom_usage = area_usage.get('Bathroom', 0)
    kitchen_usage = area_usage.get('Kitchen', 0)
    laundry_usage = area_usage.get('Laundry', 0)
    cleaning_usage = area_usage.get('Cleaning', 0)
    
    if bathroom_usage > total_usage * 0.5:
        suggestions.append(f"Bathroom usage is {round(bathroom_usage/total_usage*100)}%. Install low-flow shower heads and aerators.")
    
    if kitchen_usage > total_usage * 0.25:
        suggestions.append(f"Kitchen usage is high ({round(kitchen_usage)} L). Use water-efficient dishwashing methods.")
    
    if laundry_usage > total_usage * 0.3:
        suggestions.append(f"Laundry consumes {round(laundry_usage/total_usage*100)}%. Schedule washing hours and use full loads only.")
    
    if cleaning_usage > total_usage * 0.2:
        suggestions.append(f"Cleaning usage is {round(cleaning_usage)} L. Use mops instead of hosing floors.")
    
    # Per-student analysis
    if avg_per_student > 150:
        suggestions.append(f"Average {round(avg_per_student)} L/student is high. Target: 100-120 L/student/day.")
    elif avg_per_student < 80:
        suggestions.append(f"Excellent! Usage at {round(avg_per_student)} L/student is below recommended levels.")
    
    # Abnormal usage
    if abnormal:
        max_usage = max(d['waterUsed'] for d in data)
        suggestions.append(f"⚠️ Abnormal spike detected: {round(max_usage)} L in single entry. Inspect for leaks immediately.")
    
    # Block-specific analysis
    block_usage = defaultdict(float)
    for d in data:
        block_usage[d['block']] += d['waterUsed']
    if len(block_usage) > 1:
        max_block = max(block_usage.items(), key=lambda x: x[1])
        min_block = min(block_usage.items(), key=lambda x: x[1])
        if max_block[1] > min_block[1] * 1.5:
            suggestions.append(f"{max_block[0]} uses {round(max_block[1]/min_block[1], 1)}x more than {min_block[0]}. Investigate disparity.")
    
    # Daily trend analysis
    if len(daily_usage) >= 3:
        recent_days = list(daily_usage.values())[-3:]
        if all(recent_days[i] > recent_days[i-1] for i in range(1, len(recent_days))):
            suggestions.append("⚠️ Water usage increasing daily. Review consumption patterns urgently.")
        elif all(recent_days[i] < recent_days[i-1] for i in range(1, len(recent_days))):
            suggestions.append("✓ Great! Water usage decreasing. Keep up conservation efforts.")
    
    # General tips (only if no specific issues found)
    if len(suggestions) < 3:
        suggestions.append("Encourage students to report dripping taps immediately.")
        suggestions.append("Display water conservation posters in common areas.")
        suggestions.append("Conduct weekly water audits to identify wastage.")
    
    return jsonify({
        'totalUsage': round(total_usage, 2),
        'avgPerStudent': round(avg_per_student, 2),
        'peakTime': f"{peak_time}:00",
        'areaUsage': dict(area_usage),
        'dailyUsage': dict(daily_usage),
        'timeSeries': time_series,
        'abnormal': abnormal,
        'abnormalEntries': abnormal_entries,
        'suggestions': suggestions,
        'heatmapData': heatmap_data,
        'efficiencyScore': round(efficiency_score, 2),
        'efficiencyCategory': efficiency_category,
        'perStudentDaily': round(per_student_daily, 2),
        'tankRefillHours': tank_refill_hours,
        'weeklyUsage': round(weekly_usage, 2),
        'waterSaved': round(water_saved, 2)
    })

@app.route('/api/predict')
def predict():
    data = load_data()
    if len(data) < 3:
        return jsonify({'error': 'Need at least 3 data points for prediction'})
    
    # Group by date
    daily_usage = defaultdict(float)
    for d in data:
        daily_usage[d['date']] += d['waterUsed']
    
    dates = sorted(daily_usage.keys())
    usage_values = [daily_usage[d] for d in dates]
    
    # Prepare data for linear regression
    X = np.array(range(len(usage_values))).reshape(-1, 1)
    y = np.array(usage_values)
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Predict next day
    next_day = len(usage_values)
    prediction = model.predict([[next_day]])[0]
    
    return jsonify({
        'prediction': round(prediction, 2),
        'historicalData': [{'day': i+1, 'usage': usage_values[i]} for i in range(len(usage_values))]
    })

if __name__ == '__main__':
    os.makedirs('data', exist_ok=True)
    app.run(debug=True)
