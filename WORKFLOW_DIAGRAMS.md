# Water Usage Analysis System - Workflow Diagrams

## Complete System Workflow Diagram

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                    WATER USAGE ANALYSIS SYSTEM - COMPLETE WORKFLOW            ║
╚═══════════════════════════════════════════════════════════════════════════════╝

                                    START
                                      │
                                      ▼
                        ┌─────────────────────────┐
                        │   User Opens Browser    │
                        │   http://localhost:5000 │
                        └─────────────────────────┘
                                      │
                                      ▼
                        ┌─────────────────────────┐
                        │  Flask Server Running   │
                        │  app.py initialized     │
                        └─────────────────────────┘
                                      │
                                      ▼
                        ┌─────────────────────────┐
                        │   HOME PAGE LOADS       │
                        │   (index.html)          │
                        └─────────────────────────┘
                                      │
                    ┌─────────────────┼─────────────────┐
                    │                 │                 │
                    ▼                 ▼                 ▼
        ┌───────────────────┐ ┌──────────────┐ ┌──────────────┐
        │   DATA ENTRY      │ │  DASHBOARD   │ │  PREDICTION  │
        │   WORKFLOW        │ │  WORKFLOW    │ │  WORKFLOW    │
        └───────────────────┘ └──────────────┘ └──────────────┘
                    │                 │                 │
                    │                 │                 │
                    ▼                 ▼                 ▼
        ┌───────────────────┐ ┌──────────────┐ ┌──────────────┐
        │ 1. Fill Form      │ │ 1. Load Page │ │ 1. Load Page │
        │ 2. Validate       │ │ 2. Fetch API │ │ 2. Fetch API │
        │ 3. Submit         │ │ 3. Process   │ │ 3. Train ML  │
        │ 4. Calculate      │ │ 4. Render    │ │ 4. Predict   │
        │ 5. Store JSON     │ │ 5. Display   │ │ 5. Display   │
        └───────────────────┘ └──────────────┘ └──────────────┘
                    │                 │                 │
                    └─────────────────┼─────────────────┘
                                      │
                                      ▼
                        ┌─────────────────────────┐
                        │   DATA PERSISTED IN     │
                        │   water_data.json       │
                        └─────────────────────────┘
                                      │
                                      ▼
                                     END
```

---

## Detailed Module Workflows

### 1. DATA ENTRY MODULE - Step by Step

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         DATA ENTRY WORKFLOW                                   ║
╚═══════════════════════════════════════════════════════════════════════════════╝

STEP 1: Navigation
┌─────────────────────────────────────────────────────────────────────────────┐
│  User clicks "Data Entry" link                                              │
│  Browser sends: GET /form                                                   │
│  Flask returns: form.html                                                   │
└─────────────────────────────────────────────────────────────────────────────┘
                                      ↓
STEP 2: Form Display
┌─────────────────────────────────────────────────────────────────────────────┐
│  Form fields displayed:                                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ Date:              [2024-01-15]                                     │   │
│  │ Time:              [08:30]                                          │   │
│  │ Tank Capacity:     [5000] liters                                    │   │
│  │ Previous Level:    [4500] liters                                    │   │
│  │ Current Level:     [3200] liters                                    │   │
│  │ Students:          [50]                                             │   │
│  │ Usage Area:        [Bathroom ▼]                                     │   │
│  │ Hostel Block:      [Block A]                                        │   │
│  │                                                                     │   │
│  │                    [Submit Data]                                    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
                                      ↓
STEP 3: Client-Side Validation (JavaScript)
┌─────────────────────────────────────────────────────────────────────────────┐
│  Validation Checks:                                                         │
│  ✓ All fields filled?                                                       │
│  ✓ Current Level ≤ Previous Level?                                          │
│  ✓ Previous Level ≤ Tank Capacity?                                          │
│  ✓ Numbers are positive?                                                    │
│                                                                             │
│  If FAIL → Show error message, stop submission                              │
│  If PASS → Continue to next step                                            │
└─────────────────────────────────────────────────────────────────────────────┘
                                      ↓
STEP 4: Data Submission
┌─────────────────────────────────────────────────────────────────────────────┐
│  JavaScript sends POST request to /api/submit                               │
│  Content-Type: application/json                                             │
│                                                                             │
│  Request Body:                                                              │
│  {                                                                          │
│    "date": "2024-01-15",                                                    │
│    "time": "08:30",                                                         │
│    "tankCapacity": 5000,                                                    │
│    "prevLevel": 4500,                                                       │
│    "currLevel": 3200,                                                       │
│    "students": 50,                                                          │
│    "area": "Bathroom",                                                      │
│    "block": "Block A"                                                       │
│  }                                                                          │
└─────────────────────────────────────────────────────────────────────────────┘
                                      ↓
STEP 5: Server Processing (Flask)
┌─────────────────────────────────────────────────────────────────────────────┐
│  @app.route('/api/submit', methods=['POST'])                                │
│  def submit_data():                                                         │
│                                                                             │
│    1. Receive JSON data                                                     │
│    2. Parse request.json                                                    │
│    3. Calculate: waterUsed = prevLevel - currLevel                          │
│       → waterUsed = 4500 - 3200 = 1300 liters                               │
│    4. Create entry object with timestamp                                    │
│    5. Load existing data from water_data.json                               │
│    6. Append new entry to list                                              │
│    7. Save updated list to water_data.json                                  │
│    8. Return success response                                               │
└─────────────────────────────────────────────────────────────────────────────┘
                                      ↓
STEP 6: Data Storage
┌─────────────────────────────────────────────────────────────────────────────┐
│  water_data.json updated:                                                   │
│  [                                                                          │
│    ... existing entries ...,                                                │
│    {                                                                        │
│      "date": "2024-01-15",                                                  │
│      "time": "08:30",                                                       │
│      "tankCapacity": 5000,                                                  │
│      "prevLevel": 4500,                                                     │
│      "currLevel": 3200,                                                     │
│      "waterUsed": 1300,          ← CALCULATED                               │
│      "students": 50,                                                        │
│      "area": "Bathroom",                                                    │
│      "block": "Block A",                                                    │
│      "timestamp": "2024-01-15T08:30:00"  ← ADDED                            │
│    }                                                                        │
│  ]                                                                          │
└─────────────────────────────────────────────────────────────────────────────┘
                                      ↓
STEP 7: Response & Feedback
┌─────────────────────────────────────────────────────────────────────────────┐
│  Server Response:                                                           │
│  {                                                                          │
│    "success": true,                                                         │
│    "waterUsed": 1300                                                        │
│  }                                                                          │
│                                                                             │
│  Browser displays:                                                          │
│  ┌───────────────────────────────────────────────────────────────────┐     │
│  │ ✓ Data submitted successfully!                                    │     │
│  │   Water used: 1300.00 liters                                      │     │
│  └───────────────────────────────────────────────────────────────────┘     │
│                                                                             │
│  Form resets, ready for next entry                                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

### 2. DASHBOARD MODULE - Step by Step

```
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         DASHBOARD WORKFLOW                                    ║
╚═══════════════════════════════════════════════════════════════════════════════╝

STEP 1: Page Load
┌─────────────────────────────────────────────────────────────────────────────┐
│  User clicks "Dashboard"                                                    │
│  Browser: GET /dashboard                                                    │
│  Flask: Returns dashboard.html                                              │
│  Page loads with empty placeholders                                         │
└─────────────────────────────────────────────────────────────────────────────┘
                                      ↓
STEP 2: JavaScript Initialization
┌─────────────────────────────────────────────────────────────────────────────┐
│  <script>                                                                   │
│    loadDashboard() function executes                                        │
│    Sends: GET /api/analytics                                                │
│  </script>                                                                  │
└─────────────────────────────────────────────────────────────────────────────┘
                                      ↓
STEP 3: Data Retrieval
┌─────────────────────────────────────────────────────────────────────────────┐
│  Flask reads water_data.json                                                │
│  Loads all entries into memory                                              │
│                                                                             │
│  Example data:                                                              │
│  [                                                                          │
│    {date: "2024-01-15", time: "08:30", waterUsed: 1300, ...},             │
│    {date: "2024-01-15", time: "12:00", waterUsed: 800, ...},              │
│    {date: "2024-01-16", time: "08:00", waterUsed: 1500, ...},             │
│    ...                                                                      │
│  ]                                                                          │
└─────────────────────────────────────────────────────────────────────────────┘
                                      ↓
STEP 4: Analytics Processing
┌─────────────────────────────────────────────────────────────────────────────┐
│  CALCULATION 1: Total Usage                                                 │
│  ────────────────────────────────────────────────────────────────────────   │
│  total_usage = sum(all waterUsed values)                                    │
│  = 1300 + 800 + 1500 + ... = 15,600 liters                                  │
│                                                                             │
│  CALCULATION 2: Peak Time                                                   │
│  ────────────────────────────────────────────────────────────────────────   │
│  Group by hour:                                                             │
│    08:00 → 2800L                                                            │
│    12:00 → 1500L                                                            │
│    18:00 → 2100L                                                            │
│  Peak = 08:00 (highest usage)                                               │
│                                                                             │
│  CALCULATION 3: Average per Student                                         │
│  ────────────────────────────────────────────────────────────────────────   │
│  total_students = sum(all students)                                         │
│  avg = total_usage / total_students                                         │
│  = 15,600 / 600 = 26 liters/student                                         │
│                                                                             │
│  CALCULATION 4: Usage by Area                                               │
│  ────────────────────────────────────────────────────────────────────────   │
│  Bathroom: 8500L                                                            │
│  Kitchen:  4200L                                                            │
│  Laundry:  2100L                                                            │
│  Cleaning:  800L                                                            │
│                                                                             │
│  CALCULATION 5: Daily Usage                                                 │
│  ────────────────────────────────────────────────────────────────────────   │
│  2024-01-15: 5200L                                                          │
│  2024-01-16: 5400L                                                          │
│  2024-01-17: 5000L                                                          │
│                                                                             │
│  CALCULATION 6: Abnormal Detection                                          │
│  ────────────────────────────────────────────────────────────────────────   │
│  avg_usage = 15600 / 12 = 1300L                                             │
│  threshold = 1300 × 1.4 = 1820L                                             │
│  Check: any entry > 1820L? → NO                                             │
│  abnormal = false                                                           │
│                                                                             │
│  CALCULATION 7: Generate Suggestions                                        │
│  ────────────────────────────────────────────────────────────────────────   │
│  • Morning usage high? → Add stagger schedule tip                           │
│  • Laundry usage high? → Add washing hours tip                              │
│  • Abnormal detected? → Add leak check tip                                  │
│  • Always add: Install low-flow fixtures                                    │
└─────────────────────────────────────────────────────────────────────────────┘
                                      ↓
STEP 5: JSON Response
┌─────────────────────────────────────────────────────────────────────────────┐
│  Flask returns:                                                             │
│  {                                                                          │
│    "totalUsage": 15600,                                                     │
│    "avgPerStudent": 26,                                                     │
│    "peakTime": "08:00",                                                     │
│    "areaUsage": {                                                           │
│      "Bathroom": 8500,                                                      │
│      "Kitchen": 4200,                                                       │
│      "Laundry": 2100,                                                       │
│      "Cleaning": 800                                                        │
│    },                                                                       │
│    "dailyUsage": {                                                          │
│      "2024-01-15": 5200,                                                    │
│      "2024-01-16": 5400,                                                    │
│      "2024-01-17": 5000                                                     │
│    },                                                                       │
│    "timeSeries": [...],                                                     │
│    "abnormal": false,                                                       │
│    "suggestions": [...]                                                     │
│  }                                                                          │
└─────────────────────────────────────────────────────────────────────────────┘
                                      ↓
STEP 6: UI Rendering
┌─────────────────────────────────────────────────────────────────────────────┐
│  JavaScript processes response:                                             │
│                                                                             │
│  1. UPDATE STATISTICS CARDS                                                 │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Total Water Usage    Peak Usage Time    Avg per Student           │   │
│  │     15,600 L              08:00              26 L                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  2. CREATE CHART 1: Water Usage vs Time (Line Chart)                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Usage (L)                                                          │   │
│  │  1500 ┤     ╭─╮                                                     │   │
│  │  1000 ┤   ╭─╯ ╰─╮                                                   │   │
│  │   500 ┤ ╭─╯     ╰─╮                                                 │   │
│  │     0 ┴─────────────────────────────────────────────────────────    │   │
│  │       08:30  12:00  18:00  (Time)                                   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  3. CREATE CHART 2: Daily Consumption (Bar Chart)                           │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Usage (L)                                                          │   │
│  │  6000 ┤                                                             │   │
│  │  4000 ┤  ████    ████    ████                                       │   │
│  │  2000 ┤  ████    ████    ████                                       │   │
│  │     0 ┴──────────────────────────────────────────────────────────   │   │
│  │         Jan 15  Jan 16  Jan 17                                      │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  4. CREATE CHART 3: Usage by Area (Pie Chart)                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │              ╭─────────╮                                            │   │
│  │            ╱   Bathroom  ╲                                          │   │
│  │          ╱      54%       ╲                                         │   │
│  │         │                  │                                        │   │
│  │         │  Kitchen  Laundry│                                        │   │
│  │          ╲   27%     14%  ╱                                         │   │
│  │            ╲           ╱                                            │   │
│  │              ╰─────────╯                                            │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  5. DISPLAY SUGGESTIONS                                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  💡 Conservation Suggestions                                        │   │
│  │  • Morning water usage is very high. Stagger bathing schedules.    │   │
│  │  • Install low-flow shower heads to reduce consumption.             │   │
│  │  • Encourage students to report dripping taps immediately.          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

