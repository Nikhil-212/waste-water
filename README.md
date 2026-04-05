# Water Usage Analysis System

A full-stack web application for analyzing daily water usage patterns and conservation measures in hostels.

## Features

- **Data Entry**: Record water usage data with tank levels, time, and usage areas
- **Analytics Dashboard**: Visualize consumption patterns with interactive charts
- **ML Prediction**: Predict future water usage using Linear Regression
- **Abnormal Detection**: Automatic alerts for unusual water consumption
- **Dynamic Suggestions**: Intelligent, data-driven conservation recommendations that adapt to your actual usage patterns

## Technology Stack

- **Frontend**: HTML, CSS, JavaScript, Chart.js
- **Backend**: Python Flask
- **Machine Learning**: scikit-learn (Linear Regression)
- **Data Storage**: JSON files (no database required)

## Installation

1. **Install Python dependencies**:
```bash
pip install -r requirements.txt
```

2. **Run the application**:
```bash
python app.py
```

3. **Open your browser** and navigate to:
```
http://127.0.0.1:5000
```

## Project Structure

```
water-usage-app/
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
├── templates/
│   ├── index.html         # Home page
│   ├── form.html          # Data entry form
│   ├── dashboard.html     # Analytics dashboard
│   └── prediction.html    # Prediction page
├── static/
│   ├── style.css          # Stylesheet
│   └── script.js          # JavaScript
└── data/
    └── water_data.json    # Data storage
```

## Usage

### 1. Enter Data
- Navigate to **Data Entry** page
- Fill in water usage details:
  - Date and Time
  - Tank capacity and water levels
  - Number of students
  - Usage area (Bathroom, Kitchen, Laundry, Cleaning)
  - Hostel block
- Submit the form

### 2. View Dashboard
- Navigate to **Dashboard** page
- View statistics:
  - Total water usage
  - Peak usage time
  - Average per student
- Analyze charts:
  - Water usage vs time
  - Daily consumption
  - Usage by area
- Read conservation suggestions

### 3. Check Predictions
- Navigate to **Prediction** page
- View AI-predicted water usage for tomorrow
- Requires at least 3 days of historical data

## Key Calculations

**Water Used** = Previous Water Level - Current Water Level

**Abnormal Usage** = Usage > 40% above average

**Prediction Model** = Linear Regression on historical daily usage

## Future Enhancements

- Integration with Supabase database
- Real-time monitoring
- Mobile app
- Advanced ML models (LSTM, Prophet)
- Multi-hostel comparison
- Water quality tracking

## License

Educational Project - Free to use and modify

## Author

Water Conservation Initiative 2024
