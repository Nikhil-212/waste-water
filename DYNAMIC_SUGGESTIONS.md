# Dynamic Suggestion System Documentation

## Overview

The Water Usage Analysis System now features a **fully dynamic suggestion engine** that generates personalized conservation recommendations based on actual usage patterns in your data.

---

## How It Works

### Before (Static Suggestions)
❌ Same suggestions shown to everyone regardless of actual usage patterns
❌ Generic advice not tailored to specific problems
❌ No actionable insights based on data

### After (Dynamic Suggestions)
✅ Analyzes actual water usage patterns
✅ Generates specific, actionable recommendations
✅ Adapts to different usage scenarios
✅ Provides quantitative insights with percentages and volumes

---

## Suggestion Categories

### 1. Time-Based Analysis

**Morning Usage (6 AM - 9 AM)**
- Triggers if: Morning usage > 40% of total
- Example: "Morning usage is 45% of total. Stagger bathing schedules between 6-9 AM."

**Evening Usage (6 PM - 9 PM)**
- Triggers if: Evening usage > 35% of total
- Example: "Evening peak detected (2500 L). Distribute activities across different times."

**Night Usage (10 PM - 5 AM)**
- Triggers if: Night usage > 15% of total
- Example: "High night usage detected (800 L). Check for leaks or unauthorized usage."

---

### 2. Area-Based Analysis

**Bathroom**
- Triggers if: Bathroom usage > 50% of total
- Example: "Bathroom usage is 55%. Install low-flow shower heads and aerators."

**Kitchen**
- Triggers if: Kitchen usage > 25% of total
- Example: "Kitchen usage is high (1200 L). Use water-efficient dishwashing methods."

**Laundry**
- Triggers if: Laundry usage > 30% of total
- Example: "Laundry consumes 35%. Schedule washing hours and use full loads only."

**Cleaning**
- Triggers if: Cleaning usage > 20% of total
- Example: "Cleaning usage is 950 L. Use mops instead of hosing floors."

---

### 3. Per-Student Analysis

**High Usage**
- Triggers if: Average > 150 L/student
- Example: "Average 165 L/student is high. Target: 100-120 L/student/day."

**Excellent Usage**
- Triggers if: Average < 80 L/student
- Example: "Excellent! Usage at 75 L/student is below recommended levels."

---

### 4. Abnormal Usage Detection

**Spike Detection**
- Triggers if: Any entry > 140% of average
- Example: "⚠️ Abnormal spike detected: 2800 L in single entry. Inspect for leaks immediately."

---

### 5. Block Comparison

**Disparity Analysis**
- Triggers if: Highest block uses 1.5x more than lowest
- Example: "Block A uses 2.3x more than Block C. Investigate disparity."

---

### 6. Trend Analysis

**Increasing Trend**
- Triggers if: Last 3 days show continuous increase
- Example: "⚠️ Water usage increasing daily. Review consumption patterns urgently."

**Decreasing Trend**
- Triggers if: Last 3 days show continuous decrease
- Example: "✓ Great! Water usage decreasing. Keep up conservation efforts."

---

## Example Scenarios

### Scenario 1: High Morning Bathroom Usage
**Data Pattern:**
- Morning (6-9 AM): 3000 L (50% of total)
- Bathroom: 4000 L (65% of total)
- Average: 180 L/student

**Generated Suggestions:**
1. "Morning usage is 50% of total. Stagger bathing schedules between 6-9 AM."
2. "Bathroom usage is 65%. Install low-flow shower heads and aerators."
3. "Average 180 L/student is high. Target: 100-120 L/student/day."

---

### Scenario 2: Laundry-Heavy Usage
**Data Pattern:**
- Laundry: 2500 L (45% of total)
- Evening: 2000 L (36% of total)

**Generated Suggestions:**
1. "Laundry consumes 45%. Schedule washing hours and use full loads only."
2. "Evening peak detected (2000 L). Distribute activities across different times."

---

### Scenario 3: Abnormal Spike with Block Disparity
**Data Pattern:**
- One entry: 3500 L (200% of average)
- Block A: 8000 L
- Block B: 3000 L

**Generated Suggestions:**
1. "⚠️ Abnormal spike detected: 3500 L in single entry. Inspect for leaks immediately."
2. "Block A uses 2.7x more than Block B. Investigate disparity."

---

### Scenario 4: Excellent Conservation
**Data Pattern:**
- Average: 70 L/student
- Decreasing trend over 3 days
- No abnormal usage

**Generated Suggestions:**
1. "Excellent! Usage at 70 L/student is below recommended levels."
2. "✓ Great! Water usage decreasing. Keep up conservation efforts."
3. "Encourage students to report dripping taps immediately."

---

## Thresholds Reference

| Metric | Threshold | Action |
|--------|-----------|--------|
| Morning Usage | > 40% | Suggest staggering |
| Evening Usage | > 35% | Suggest distribution |
| Night Usage | > 15% | Check for leaks |
| Bathroom | > 50% | Install low-flow fixtures |
| Kitchen | > 25% | Efficient dishwashing |
| Laundry | > 30% | Schedule washing |
| Cleaning | > 20% | Use mops |
| Per Student | > 150 L | Reduce consumption |
| Per Student | < 80 L | Praise efficiency |
| Abnormal | > 140% avg | Inspect immediately |
| Block Disparity | > 1.5x | Investigate |

---

## Benefits of Dynamic Suggestions

### 1. Actionable Insights
- Specific numbers and percentages
- Clear targets and goals
- Prioritized recommendations

### 2. Data-Driven
- Based on actual usage patterns
- Adapts to different scenarios
- No generic advice

### 3. Comprehensive Coverage
- Time-based analysis
- Area-based analysis
- Student-level metrics
- Block comparisons
- Trend detection

### 4. Smart Fallback
- Shows general tips only if no specific issues found
- Ensures users always get value
- Prevents empty suggestion lists

---

## Testing the System

### Test Case 1: Enter High Morning Bathroom Usage
```
Date: 2024-01-15
Time: 08:00
Area: Bathroom
Water Used: 2000 L
Students: 50
```
**Expected:** Morning and bathroom suggestions

### Test Case 2: Enter High Laundry Usage
```
Date: 2024-01-15
Time: 14:00
Area: Laundry
Water Used: 1800 L
Students: 40
```
**Expected:** Laundry-specific suggestions

### Test Case 3: Enter Abnormal Spike
```
Date: 2024-01-15
Time: 03:00
Area: Bathroom
Water Used: 3500 L
Students: 50
```
**Expected:** Abnormal usage alert + night usage warning

### Test Case 4: Multiple Blocks
```
Block A: 5000 L total
Block B: 2000 L total
```
**Expected:** Block disparity suggestion

---

## Customization

You can adjust thresholds in `app.py`:

```python
# Time thresholds
morning_threshold = 0.4  # 40%
evening_threshold = 0.35 # 35%
night_threshold = 0.15   # 15%

# Area thresholds
bathroom_threshold = 0.5  # 50%
kitchen_threshold = 0.25  # 25%
laundry_threshold = 0.3   # 30%
cleaning_threshold = 0.2  # 20%

# Per-student thresholds
high_usage = 150  # liters
excellent_usage = 80  # liters

# Abnormal detection
abnormal_multiplier = 1.4  # 140% of average

# Block disparity
disparity_ratio = 1.5  # 1.5x difference
```

---

## Summary

The dynamic suggestion system transforms generic advice into **personalized, data-driven recommendations** that help hostels identify specific water conservation opportunities and take targeted action.

**Key Features:**
- ✅ Fully dynamic based on actual data
- ✅ Quantitative insights with numbers
- ✅ Multiple analysis dimensions
- ✅ Actionable recommendations
- ✅ Smart fallback for edge cases
