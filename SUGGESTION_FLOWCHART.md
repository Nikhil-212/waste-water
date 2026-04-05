# Dynamic Suggestion Generation Flowchart

## Complete Suggestion Engine Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    USER ENTERS DATA                              │
│  Date, Time, Area, Water Levels, Students, Block                │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                    DATA STORED IN JSON                           │
│  All historical entries accumulated                              │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              USER OPENS DASHBOARD                                │
│  Triggers: GET /api/analytics                                    │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              LOAD ALL DATA FROM JSON                             │
│  Read all historical water usage entries                         │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│           CALCULATE BASIC METRICS                                │
│  • Total Usage                                                   │
│  • Average per Student                                           │
│  • Peak Time                                                     │
│  • Usage by Area                                                 │
│  • Usage by Date                                                 │
│  • Usage by Block                                                │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│         DYNAMIC SUGGESTION ENGINE STARTS                         │
│         Initialize: suggestions = []                             │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
        ┌────────────────────┴────────────────────┐
        │                                         │
        ▼                                         ▼
┌──────────────────┐                    ┌──────────────────┐
│  TIME ANALYSIS   │                    │  AREA ANALYSIS   │
└────────┬─────────┘                    └────────┬─────────┘
         │                                       │
         ├─→ Morning > 40%? ──YES──→ Add Suggestion
         │                    NO
         │                    ↓
         ├─→ Evening > 35%? ──YES──→ Add Suggestion
         │                    NO
         │                    ↓
         └─→ Night > 15%? ────YES──→ Add Suggestion
                             NO
                             ↓
                        (Skip)

                                                  │
                                                  ├─→ Bathroom > 50%? ──YES──→ Add
                                                  │                      NO
                                                  │                      ↓
                                                  ├─→ Kitchen > 25%? ────YES──→ Add
                                                  │                      NO
                                                  │                      ↓
                                                  ├─→ Laundry > 30%? ────YES──→ Add
                                                  │                      NO
                                                  │                      ↓
                                                  └─→ Cleaning > 20%? ───YES──→ Add
                                                                         NO
                                                                         ↓
                                                                    (Skip)

        │                                         │
        └────────────────────┬────────────────────┘
                             │
                             ▼
        ┌────────────────────┴────────────────────┐
        │                                         │
        ▼                                         ▼
┌──────────────────┐                    ┌──────────────────┐
│ STUDENT ANALYSIS │                    │ ANOMALY DETECTION│
└────────┬─────────┘                    └────────┬─────────┘
         │                                       │
         ├─→ Avg > 150 L? ────YES──→ Add Warning
         │                    NO
         │                    ↓
         └─→ Avg < 80 L? ─────YES──→ Add Praise
                             NO
                             ↓
                        (Skip)

                                                  │
                                                  └─→ Any entry > 140% avg? ──YES──→ Add Alert
                                                                              NO
                                                                              ↓
                                                                         (Skip)

        │                                         │
        └────────────────────┬────────────────────┘
                             │
                             ▼
        ┌────────────────────┴────────────────────┐
        │                                         │
        ▼                                         ▼
┌──────────────────┐                    ┌──────────────────┐
│ BLOCK COMPARISON │                    │ TREND ANALYSIS   │
└────────┬─────────┘                    └────────┬─────────┘
         │                                       │
         └─→ Max block > 1.5x min? ──YES──→ Add Comparison
                             NO
                             ↓
                        (Skip)

                                                  │
                                                  ├─→ 3 days increasing? ──YES──→ Add Warning
                                                  │                        NO
                                                  │                        ↓
                                                  └─→ 3 days decreasing? ──YES──→ Add Praise
                                                                           NO
                                                                           ↓
                                                                      (Skip)

        │                                         │
        └────────────────────┬────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              CHECK SUGGESTION COUNT                              │
│  If suggestions < 3, add general tips                           │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              RETURN SUGGESTIONS ARRAY                            │
│  [                                                               │
│    "Morning usage is 45% of total. Stagger schedules.",        │
│    "Bathroom usage is 65%. Install low-flow fixtures.",        │
│    "Average 180 L/student is high. Target: 100-120 L."         │
│  ]                                                               │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│              DISPLAY ON DASHBOARD                                │
│  User sees personalized, data-driven recommendations            │
└─────────────────────────────────────────────────────────────────┘
```

---

## Decision Tree for Each Analysis Type

### 1. Time-Based Decisions

```
Morning Usage Analysis
├─ Calculate: morning_usage / total_usage
├─ Is ratio > 0.40?
│  ├─ YES → Add: "Morning usage is X%. Stagger bathing schedules."
│  └─ NO  → Skip
│
Evening Usage Analysis
├─ Calculate: evening_usage / total_usage
├─ Is ratio > 0.35?
│  ├─ YES → Add: "Evening peak detected (X L). Distribute activities."
│  └─ NO  → Skip
│
Night Usage Analysis
├─ Calculate: night_usage / total_usage
├─ Is ratio > 0.15?
│  ├─ YES → Add: "High night usage (X L). Check for leaks."
│  └─ NO  → Skip
```

### 2. Area-Based Decisions

```
For Each Area (Bathroom, Kitchen, Laundry, Cleaning):
├─ Calculate: area_usage / total_usage
├─ Compare against threshold
│  ├─ Bathroom > 50%? → Add bathroom suggestion
│  ├─ Kitchen > 25%?  → Add kitchen suggestion
│  ├─ Laundry > 30%?  → Add laundry suggestion
│  └─ Cleaning > 20%? → Add cleaning suggestion
```

### 3. Student-Level Decisions

```
Per-Student Analysis
├─ Calculate: total_usage / total_students
├─ Check value
│  ├─ > 150 L? → Add: "Average X L/student is high. Target: 100-120 L."
│  ├─ < 80 L?  → Add: "Excellent! Usage at X L/student is below recommended."
│  └─ 80-150?  → Skip (normal range)
```

### 4. Anomaly Detection

```
Abnormal Usage Detection
├─ Calculate: average_usage = total / count
├─ Calculate: threshold = average × 1.4
├─ For each entry:
│  └─ If entry.waterUsed > threshold
│     └─ Add: "⚠️ Abnormal spike: X L detected. Inspect immediately."
```

### 5. Block Comparison

```
Block Disparity Analysis
├─ Group usage by block
├─ Find max_block and min_block
├─ Calculate: ratio = max_usage / min_usage
├─ Is ratio > 1.5?
│  ├─ YES → Add: "Block A uses Xx more than Block B. Investigate."
│  └─ NO  → Skip
```

### 6. Trend Analysis

```
Trend Detection (requires 3+ days)
├─ Get last 3 days of usage
├─ Check pattern:
│  ├─ All increasing? → Add: "⚠️ Usage increasing daily. Review urgently."
│  ├─ All decreasing? → Add: "✓ Usage decreasing. Keep up efforts."
│  └─ Mixed pattern?  → Skip
```

---

## Example Execution Trace

### Input Data:
```json
[
  {"time": "08:00", "area": "Bathroom", "waterUsed": 2000, "students": 50, "block": "A"},
  {"time": "14:00", "area": "Laundry", "waterUsed": 1500, "students": 50, "block": "A"},
  {"time": "19:00", "area": "Kitchen", "waterUsed": 500, "students": 50, "block": "A"}
]
```

### Execution Flow:

```
1. Load Data ✓
   Total: 4000 L, Students: 150, Avg: 26.67 L/student

2. Time Analysis:
   Morning (6-9): 2000 L → 50% of total → TRIGGER ✓
   Evening (18-21): 500 L → 12.5% of total → SKIP
   Night (22-5): 0 L → 0% of total → SKIP

3. Area Analysis:
   Bathroom: 2000 L → 50% of total → TRIGGER ✓
   Kitchen: 500 L → 12.5% of total → SKIP
   Laundry: 1500 L → 37.5% of total → TRIGGER ✓
   Cleaning: 0 L → 0% of total → SKIP

4. Student Analysis:
   Avg: 26.67 L/student → Normal range → SKIP

5. Anomaly Detection:
   Avg: 1333 L, Threshold: 1866 L
   Max entry: 2000 L → Above threshold → TRIGGER ✓

6. Block Comparison:
   Only 1 block → SKIP

7. Trend Analysis:
   Only 1 day of data → SKIP

8. Final Suggestions:
   [
     "Morning usage is 50% of total. Stagger bathing schedules.",
     "Bathroom usage is 50%. Install low-flow shower heads.",
     "Laundry consumes 38%. Schedule washing hours.",
     "⚠️ Abnormal spike: 2000 L detected. Inspect immediately."
   ]
```

---

## Summary

The dynamic suggestion engine:

1. ✅ **Analyzes** multiple dimensions of your data
2. ✅ **Evaluates** each metric against thresholds
3. ✅ **Generates** only relevant suggestions
4. ✅ **Includes** specific numbers and percentages
5. ✅ **Provides** actionable recommendations
6. ✅ **Adapts** to different usage patterns

**Result:** Personalized, intelligent water conservation advice! 💧🎯
