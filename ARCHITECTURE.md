# Water Usage Analysis System - Architecture Documentation

## Table of Contents
1. System Overview
2. Technology Stack
3. Architecture Layers
4. End-to-End Workflow
5. Data Flow Diagrams
6. Component Interaction
7. API Endpoints
8. Machine Learning Pipeline

---

## 1. System Overview

The Water Usage Analysis System is a full-stack web application designed to monitor, analyze, and predict water consumption patterns in hostel environments. The system operates without a database, using JSON file storage for data persistence.

### Key Objectives
- Track daily water usage across multiple hostel blocks
- Identify peak consumption periods
- Detect abnormal usage patterns
- Predict future water demand using ML
- Provide actionable conservation recommendations

---

## 2. Technology Stack

### Frontend Layer
```
┌─────────────────────────────────────┐
│         Frontend Stack              │
├─────────────────────────────────────┤
│ HTML5        - Structure            │
│ CSS3         - Styling & Layout     │
│ JavaScript   - Client Logic         │
│ Chart.js     - Data Visualization   │
└─────────────────────────────────────┘
```

### Backend Layer
```
┌─────────────────────────────────────┐
│         Backend Stack               │
├─────────────────────────────────────┤
│ Python 3.x   - Core Language        │
│ Flask        - Web Framework        │
│ JSON         - Data Storage         │
└─────────────────────────────────────┘
```

### Machine Learning Layer
```
┌─────────────────────────────────────┐
│      ML/Analytics Stack             │
├─────────────────────────────────────┤
│ scikit-learn - ML Models            │
│ NumPy        - Numerical Computing  │
│ Linear Reg.  - Prediction Algorithm │
└─────────────────────────────────────┘
```

---

## 3. Architecture Layers

### Three-Tier Architecture

```
┌────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                       │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  │
│  │   Home   │  │   Form   │  │Dashboard │  │Prediction│  │
│  │   Page   │  │   Page   │  │   Page   │  │   Page   │  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘  │
│       HTML + CSS + JavaScript + Chart.js                   │
└────────────────────────────────────────────────────────────┘
                            ↕ HTTP/HTTPS
┌────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                        │
│  ┌──────────────────────────────────────────────────────┐ │
│  │              Flask Web Server (app.py)               │ │
│  ├──────────────────────────────────────────────────────┤ │
│  │  Routes:                                             │ │
│  │  • / (Home)           • /form (Data Entry)          │ │
│  │  • /dashboard         • /prediction                  │ │
│  ├──────────────────────────────────────────────────────┤ │
│  │  API Endpoints:                                      │ │
│  │  • POST /api/submit   • GET /api/analytics          │ │
│  │  • GET /api/predict                                  │ │
│  ├──────────────────────────────────────────────────────┤ │
│  │  Business Logic:                                     │ │
│  │  • Data Validation    • Usage Calculation           │ │
│  │  • Analytics Engine   • Anomaly Detection           │ │
│  │  • ML Prediction      • Suggestion Generator        │ │
│  └──────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────┘
                            ↕ File I/O
┌────────────────────────────────────────────────────────────┐
│                      DATA LAYER                             │
│  ┌──────────────────────────────────────────────────────┐ │
│  │           JSON File Storage (water_data.json)        │ │
│  ├──────────────────────────────────────────────────────┤ │
│  │  Data Structure:                                     │ │
│  │  [                                                   │ │
│  │    {                                                 │ │
│  │      "date": "2024-01-15",                          │ │
│  │      "time": "08:30",                               │ │
│  │      "tankCapacity": 5000,                          │ │
│  │      "prevLevel": 4500,                             │ │
│  │      "currLevel": 3200,                             │ │
│  │      "waterUsed": 1300,                             │ │
│  │      "students": 50,                                │ │
│  │      "area": "Bathroom",                            │ │
│  │      "block": "Block A"                             │ │
│  │    }                                                 │ │
│  │  ]                                                   │ │
│  └──────────────────────────────────────────────────────┘ │
└────────────────────────────────────────────────────────────┘
```

---

## 4. End-to-End Workflow

### Complete System Flow

```
START
  │
  ├─→ User Opens Browser
  │
  ├─→ Navigate to http://localhost:5000
  │
  ├─→ Flask Server Renders Home Page (index.html)
  │
  ├─→ User Selects Action:
  │   │
  │   ├─→ [1] DATA ENTRY
  │   │   │
  │   │   ├─→ Navigate to /form
  │   │   ├─→ Fill Form Fields
  │   │   ├─→ Submit Form (JavaScript)
  │   │   ├─→ POST /api/submit
  │   │   ├─→ Flask Validates Data
  │   │   ├─→ Calculate: waterUsed = prevLevel - currLevel
  │   │   ├─→ Append to water_data.json
  │   │   ├─→ Return Success Response
  │   │   └─→ Display Confirmation Message
  │   │
  │   ├─→ [2] VIEW DASHBOARD
  │   │   │
  │   │   ├─→ Navigate to /dashboard
  │   │   ├─→ Page Loads (dashboard.html)
  │   │   ├─→ JavaScript: fetch('/api/analytics')
  │   │   ├─→ Flask Reads water_data.json
  │   │   ├─→ Process Analytics:
  │   │   │   ├─→ Calculate Total Usage
  │   │   │   ├─→ Find Peak Time
  │   │   │   ├─→ Calculate Avg per Student
  │   │   │   ├─→ Group by Area
  │   │   │   ├─→ Group by Date
  │   │   │   ├─→ Detect Abnormal Usage
  │   │   │   └─→ Generate Suggestions
  │   │   ├─→ Return JSON Response
  │   │   ├─→ JavaScript Renders:
  │   │   │   ├─→ Statistics Cards
  │   │   │   ├─→ Chart.js Graphs
  │   │   │   ├─→ Alert (if abnormal)
  │   │   │   └─→ Suggestions List
  │   │   └─→ Display Dashboard
  │   │
  │   └─→ [3] VIEW PREDICTION
  │       │
  │       ├─→ Navigate to /prediction
  │       ├─→ Page Loads (prediction.html)
  │       ├─→ JavaScript: fetch('/api/predict')
  │       ├─→ Flask Reads water_data.json
  │       ├─→ ML Pipeline:
  │       │   ├─→ Group Data by Date
  │       │   ├─→ Prepare Training Data (X, y)
  │       │   ├─→ Train Linear Regression Model
  │       │   ├─→ Predict Next Day Usage
  │       │   └─→ Return Prediction
  │       ├─→ JavaScript Renders:
  │       │   ├─→ Prediction Value
  │       │   └─→ Trend Chart
  │       └─→ Display Prediction
  │
END
```


## 5. Detailed Module Workflows

### 5.1 Data Entry Module Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                    DATA ENTRY WORKFLOW                       │
└─────────────────────────────────────────────────────────────┘

User                Browser              Flask Server         JSON File
 │                     │                      │                   │
 │  Click "Data Entry" │                      │                   │
 ├────────────────────>│                      │                   │
 │                     │  GET /form           │                   │
 │                     ├─────────────────────>│                   │
 │                     │                      │                   │
 │                     │  form.html           │                   │
 │                     │<─────────────────────┤                   │
 │                     │                      │                   │
 │  Fill Form Data     │                      │                   │
 ├────────────────────>│                      │                   │
 │                     │                      │                   │
 │  Click Submit       │                      │                   │
 ├────────────────────>│                      │                   │
 │                     │                      │                   │
 │                     │  Validate (JS)       │                   │
 │                     │  - Check levels      │                   │
 │                     │  - Check capacity    │                   │
 │                     │                      │                   │
 │                     │  POST /api/submit    │                   │
 │                     │  {form data}         │                   │
 │                     ├─────────────────────>│                   │
 │                     │                      │                   │
 │                     │                      │  Validate Data    │
 │                     │                      │  Calculate:       │
 │                     │                      │  waterUsed =      │
 │                     │                      │  prev - current   │
 │                     │                      │                   │
 │                     │                      │  Read JSON        │
 │                     │                      ├──────────────────>│
 │                     │                      │  Current Data     │
 │                     │                      │<──────────────────┤
 │                     │                      │                   │
 │                     │                      │  Append Entry     │
 │                     │                      ├──────────────────>│
 │                     │                      │  Write Success    │
 │                     │                      │<──────────────────┤
 │                     │                      │                   │
 │                     │  {success: true,     │                   │
 │                     │   waterUsed: 1300}   │                   │
 │                     │<─────────────────────┤                   │
 │                     │                      │                   │
 │  Success Message    │                      │                   │
 │<────────────────────┤                      │                   │
 │  "Data submitted!   │                      │                   │
 │   Water used: 1300L"│                      │                   │
 │                     │                      │                   │
```

### 5.2 Analytics Dashboard Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                  DASHBOARD WORKFLOW                          │
└─────────────────────────────────────────────────────────────┘

User              Browser            Flask Server         JSON File
 │                   │                    │                    │
 │  Click Dashboard  │                    │                    │
 ├──────────────────>│                    │                    │
 │                   │  GET /dashboard    │                    │
 │                   ├───────────────────>│                    │
 │                   │                    │                    │
 │                   │  dashboard.html    │                    │
 │                   │<───────────────────┤                    │
 │                   │                    │                    │
 │                   │  Page Loads        │                    │
 │                   │  Execute JS:       │                    │
 │                   │  loadDashboard()   │                    │
 │                   │                    │                    │
 │                   │  GET /api/analytics│                    │
 │                   ├───────────────────>│                    │
 │                   │                    │                    │
 │                   │                    │  Read JSON         │
 │                   │                    ├───────────────────>│
 │                   │                    │  All Records       │
 │                   │                    │<───────────────────┤
 │                   │                    │                    │
 │                   │                    │  ANALYTICS ENGINE  │
 │                   │                    │  ┌──────────────┐ │
 │                   │                    │  │ Calculate:   │ │
 │                   │                    │  │ • Total Usage│ │
 │                   │                    │  │ • Peak Time  │ │
 │                   │                    │  │ • Avg/Student│ │
 │                   │                    │  │ • By Area    │ │
 │                   │                    │  │ • By Date    │ │
 │                   │                    │  │ • Abnormal?  │ │
 │                   │                    │  │ • Suggestions│ │
 │                   │                    │  └──────────────┘ │
 │                   │                    │                    │
 │                   │  JSON Response:    │                    │
 │                   │  {                 │                    │
 │                   │   totalUsage,      │                    │
 │                   │   peakTime,        │                    │
 │                   │   avgPerStudent,   │                    │
 │                   │   areaUsage,       │                    │
 │                   │   dailyUsage,      │                    │
 │                   │   timeSeries,      │                    │
 │                   │   abnormal,        │                    │
 │                   │   suggestions      │                    │
 │                   │  }                 │                    │
 │                   │<───────────────────┤                    │
 │                   │                    │                    │
 │                   │  RENDER DASHBOARD  │                    │
 │                   │  ┌──────────────┐  │                    │
 │                   │  │ Update Stats │  │                    │
 │                   │  │ Create Charts│  │                    │
 │                   │  │ Show Alert   │  │                    │
 │                   │  │ List Tips    │  │                    │
 │                   │  └──────────────┘  │                    │
 │                   │                    │                    │
 │  View Dashboard   │                    │                    │
 │<──────────────────┤                    │                    │
 │  • Stats Cards    │                    │                    │
 │  • 3 Charts       │                    │                    │
 │  • Suggestions    │                    │                    │
 │                   │                    │                    │
```

### 5.3 Prediction Module Workflow

```
┌─────────────────────────────────────────────────────────────┐
│                  PREDICTION WORKFLOW                         │
└─────────────────────────────────────────────────────────────┘

User            Browser          Flask Server        ML Engine      JSON
 │                 │                  │                  │            │
 │  Click Predict  │                  │                  │            │
 ├────────────────>│                  │                  │            │
 │                 │  GET /prediction │                  │            │
 │                 ├─────────────────>│                  │            │
 │                 │                  │                  │            │
 │                 │  prediction.html │                  │            │
 │                 │<─────────────────┤                  │            │
 │                 │                  │                  │            │
 │                 │  Execute JS      │                  │            │
 │                 │  GET /api/predict│                  │            │
 │                 ├─────────────────>│                  │            │
 │                 │                  │                  │            │
 │                 │                  │  Read Data       │            │
 │                 │                  ├─────────────────────────────>│
 │                 │                  │  All Records     │            │
 │                 │                  │<─────────────────────────────┤
 │                 │                  │                  │            │
 │                 │                  │  Group by Date   │            │
 │                 │                  │  ┌────────────┐ │            │
 │                 │                  │  │ Day 1: 1200│ │            │
 │                 │                  │  │ Day 2: 1500│ │            │
 │                 │                  │  │ Day 3: 1400│ │            │
 │                 │                  │  └────────────┘ │            │
 │                 │                  │                  │            │
 │                 │                  │  Prepare ML Data │            │
 │                 │                  ├─────────────────>│            │
 │                 │                  │                  │            │
 │                 │                  │                  │ ML PIPELINE│
 │                 │                  │                  │ ┌────────┐│
 │                 │                  │                  │ │ X = [0,││
 │                 │                  │                  │ │      1,││
 │                 │                  │                  │ │      2]││
 │                 │                  │                  │ │ y = [  ││
 │                 │                  │                  │ │  1200, ││
 │                 │                  │                  │ │  1500, ││
 │                 │                  │                  │ │  1400] ││
 │                 │                  │                  │ └────────┘│
 │                 │                  │                  │            │
 │                 │                  │                  │ Train Model│
 │                 │                  │                  │ LinearReg  │
 │                 │                  │                  │ fit(X, y)  │
 │                 │                  │                  │            │
 │                 │                  │                  │ Predict    │
 │                 │                  │                  │ X_new = [3]│
 │                 │                  │                  │ y_pred =   │
 │                 │                  │                  │   1450     │
 │                 │                  │                  │            │
 │                 │                  │  Prediction: 1450│            │
 │                 │                  │<─────────────────┤            │
 │                 │                  │                  │            │
 │                 │  {               │                  │            │
 │                 │   prediction:    │                  │            │
 │                 │     1450,        │                  │            │
 │                 │   historicalData │                  │            │
 │                 │  }               │                  │            │
 │                 │<─────────────────┤                  │            │
 │                 │                  │                  │            │
 │                 │  Render Chart    │                  │            │
 │                 │  Show Prediction │                  │            │
 │                 │                  │                  │            │
 │  View Result    │                  │                  │            │
 │<────────────────┤                  │                  │            │
 │  "Predicted:    │                  │                  │            │
 │   1450 liters"  │                  │                  │            │
 │                 │                  │                  │            │
```


## 6. API Endpoints Documentation

### 6.1 Page Routes

| Route | Method | Description | Returns |
|-------|--------|-------------|---------|
| `/` | GET | Home page | index.html |
| `/form` | GET | Data entry form | form.html |
| `/dashboard` | GET | Analytics dashboard | dashboard.html |
| `/prediction` | GET | Prediction page | prediction.html |

### 6.2 API Routes

#### POST /api/submit
**Purpose:** Submit new water usage data

**Request Body:**
```json
{
  "date": "2024-01-15",
  "time": "08:30",
  "tankCapacity": 5000,
  "prevLevel": 4500,
  "currLevel": 3200,
  "students": 50,
  "area": "Bathroom",
  "block": "Block A"
}
```

**Response:**
```json
{
  "success": true,
  "waterUsed": 1300
}
```

**Processing Steps:**
1. Receive JSON data
2. Validate input fields
3. Calculate: waterUsed = prevLevel - currLevel
4. Create entry object with timestamp
5. Load existing data from JSON
6. Append new entry
7. Save to JSON file
8. Return success response

---

#### GET /api/analytics
**Purpose:** Get analytics data for dashboard

**Response:**
```json
{
  "totalUsage": 15600.50,
  "avgPerStudent": 26.5,
  "peakTime": "08:00",
  "areaUsage": {
    "Bathroom": 8500,
    "Kitchen": 4200,
    "Laundry": 2100,
    "Cleaning": 800
  },
  "dailyUsage": {
    "2024-01-15": 5200,
    "2024-01-16": 5400,
    "2024-01-17": 5000
  },
  "timeSeries": [
    {"date": "2024-01-15", "time": "08:30", "usage": 1300},
    {"date": "2024-01-15", "time": "12:00", "usage": 800}
  ],
  "abnormal": false,
  "suggestions": [
    "Install low-flow shower heads",
    "Schedule specific washing hours"
  ]
}
```

**Processing Steps:**
1. Load all data from JSON
2. Calculate total usage (sum all waterUsed)
3. Calculate average per student
4. Find peak usage time (group by hour)
5. Group usage by area
6. Group usage by date
7. Detect abnormal usage (>40% above average)
8. Generate conservation suggestions
9. Return analytics object

---

#### GET /api/predict
**Purpose:** Predict future water usage using ML

**Response:**
```json
{
  "prediction": 4200.75,
  "historicalData": [
    {"day": 1, "usage": 5200},
    {"day": 2, "usage": 5400},
    {"day": 3, "usage": 5000}
  ]
}
```

**Processing Steps:**
1. Load all data from JSON
2. Group by date and sum daily usage
3. Prepare training data (X = day indices, y = usage values)
4. Initialize Linear Regression model
5. Train model: model.fit(X, y)
6. Predict next day: model.predict([[next_day_index]])
7. Return prediction and historical data

---

## 7. Data Flow Architecture

### 7.1 Complete Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                     USER INTERFACE                           │
│  ┌────────┐  ┌────────┐  ┌──────────┐  ┌──────────┐       │
│  │  Home  │  │  Form  │  │Dashboard │  │Prediction│       │
│  └───┬────┘  └───┬────┘  └────┬─────┘  └────┬─────┘       │
└──────┼───────────┼────────────┼─────────────┼──────────────┘
       │           │            │             │
       │           │            │             │
       ▼           ▼            ▼             ▼
┌─────────────────────────────────────────────────────────────┐
│                    FLASK ROUTING LAYER                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  @app.route('/')          → render index.html        │  │
│  │  @app.route('/form')      → render form.html         │  │
│  │  @app.route('/dashboard') → render dashboard.html    │  │
│  │  @app.route('/prediction')→ render prediction.html   │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
       │           │            │             │
       │           │            │             │
       │           ▼            ▼             ▼
       │    ┌──────────────────────────────────────┐
       │    │      API ENDPOINT LAYER              │
       │    │  ┌────────────────────────────────┐  │
       │    │  │ POST /api/submit               │  │
       │    │  │  ↓                             │  │
       │    │  │  submit_data()                 │  │
       │    │  │  • Validate                    │  │
       │    │  │  • Calculate waterUsed         │  │
       │    │  │  • Store data                  │  │
       │    │  └────────────────────────────────┘  │
       │    │                                      │
       │    │  ┌────────────────────────────────┐  │
       │    │  │ GET /api/analytics             │  │
       │    │  │  ↓                             │  │
       │    │  │  analytics()                   │  │
       │    │  │  • Load data                   │  │
       │    │  │  • Process analytics           │  │
       │    │  │  • Detect anomalies            │  │
       │    │  │  • Generate suggestions        │  │
       │    │  └────────────────────────────────┘  │
       │    │                                      │
       │    │  ┌────────────────────────────────┐  │
       │    │  │ GET /api/predict               │  │
       │    │  │  ↓                             │  │
       │    │  │  predict()                     │  │
       │    │  │  • Load data                   │  │
       │    │  │  • Prepare ML data             │  │
       │    │  │  • Train model                 │  │
       │    │  │  • Generate prediction         │  │
       │    │  └────────────────────────────────┘  │
       │    └──────────────────────────────────────┘
       │                   │
       │                   ▼
       │    ┌──────────────────────────────────────┐
       │    │      BUSINESS LOGIC LAYER            │
       │    │  ┌────────────────────────────────┐  │
       │    │  │  Data Processing Functions     │  │
       │    │  │  • load_data()                 │  │
       │    │  │  • save_data()                 │  │
       │    │  │  • calculate_usage()           │  │
       │    │  │  • detect_anomaly()            │  │
       │    │  │  • generate_suggestions()      │  │
       │    │  └────────────────────────────────┘  │
       │    │                                      │
       │    │  ┌────────────────────────────────┐  │
       │    │  │  Machine Learning Pipeline     │  │
       │    │  │  • Data aggregation            │  │
       │    │  │  • Feature preparation         │  │
       │    │  │  • Model training              │  │
       │    │  │  • Prediction generation       │  │
       │    │  └────────────────────────────────┘  │
       │    └──────────────────────────────────────┘
       │                   │
       │                   ▼
       │    ┌──────────────────────────────────────┐
       │    │       DATA ACCESS LAYER              │
       │    │  ┌────────────────────────────────┐  │
       │    │  │  File Operations               │  │
       │    │  │  • Read JSON                   │  │
       │    │  │  • Write JSON                  │  │
       │    │  │  • Append data                 │  │
       │    │  └────────────────────────────────┘  │
       │    └──────────────────────────────────────┘
       │                   │
       └───────────────────┼───────────────────────
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                    DATA STORAGE LAYER                        │
│  ┌──────────────────────────────────────────────────────┐  │
│  │              water_data.json                         │  │
│  │  [                                                   │  │
│  │    {entry1}, {entry2}, {entry3}, ...                │  │
│  │  ]                                                   │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

### 7.2 Data Transformation Pipeline

```
RAW INPUT DATA
     │
     ├─→ Date: "2024-01-15"
     ├─→ Time: "08:30"
     ├─→ Tank Capacity: 5000
     ├─→ Previous Level: 4500
     ├─→ Current Level: 3200
     ├─→ Students: 50
     ├─→ Area: "Bathroom"
     └─→ Block: "Block A"
     │
     ▼
┌─────────────────────┐
│  VALIDATION LAYER   │
│  • Check required   │
│  • Validate types   │
│  • Check logic      │
└─────────────────────┘
     │
     ▼
┌─────────────────────┐
│  CALCULATION LAYER  │
│  waterUsed =        │
│  4500 - 3200 = 1300 │
└─────────────────────┘
     │
     ▼
┌─────────────────────┐
│  ENRICHMENT LAYER   │
│  • Add timestamp    │
│  • Add waterUsed    │
│  • Format data      │
└─────────────────────┘
     │
     ▼
STORED DATA OBJECT
{
  "date": "2024-01-15",
  "time": "08:30",
  "tankCapacity": 5000,
  "prevLevel": 4500,
  "currLevel": 3200,
  "waterUsed": 1300,
  "students": 50,
  "area": "Bathroom",
  "block": "Block A",
  "timestamp": "2024-01-15T08:30:00"
}
     │
     ▼
┌─────────────────────┐
│  PERSISTENCE LAYER  │
│  Append to JSON     │
└─────────────────────┘
     │
     ▼
water_data.json
```


## 8. Machine Learning Pipeline

### 8.1 Linear Regression Model Architecture

```
┌─────────────────────────────────────────────────────────────┐
│              MACHINE LEARNING PIPELINE                       │
└─────────────────────────────────────────────────────────────┘

STEP 1: DATA COLLECTION
┌──────────────────────────────────┐
│  Load from water_data.json       │
│  [                               │
│    {date: "2024-01-15", ...},   │
│    {date: "2024-01-15", ...},   │
│    {date: "2024-01-16", ...},   │
│    {date: "2024-01-17", ...}    │
│  ]                               │
└──────────────────────────────────┘
            ↓
STEP 2: DATA AGGREGATION
┌──────────────────────────────────┐
│  Group by Date & Sum Usage       │
│  {                               │
│    "2024-01-15": 5200,          │
│    "2024-01-16": 5400,          │
│    "2024-01-17": 5000,          │
│    "2024-01-18": 4800           │
│  }                               │
└──────────────────────────────────┘
            ↓
STEP 3: FEATURE ENGINEERING
┌──────────────────────────────────┐
│  Create Training Arrays          │
│                                  │
│  X (Days):    y (Usage):        │
│  [[0],        [5200,            │
│   [1],         5400,            │
│   [2],         5000,            │
│   [3]]         4800]            │
│                                  │
│  Shape: (4, 1)  Shape: (4,)     │
└──────────────────────────────────┘
            ↓
STEP 4: MODEL TRAINING
┌──────────────────────────────────┐
│  from sklearn.linear_model       │
│  import LinearRegression         │
│                                  │
│  model = LinearRegression()      │
│  model.fit(X, y)                 │
│                                  │
│  Learn: y = mx + b               │
│  where:                          │
│    m = slope (trend)             │
│    b = intercept (baseline)      │
└──────────────────────────────────┘
            ↓
STEP 5: PREDICTION
┌──────────────────────────────────┐
│  X_new = [[4]]  (Day 5)         │
│                                  │
│  y_pred = model.predict(X_new)   │
│                                  │
│  Result: 4600 liters             │
└──────────────────────────────────┘
            ↓
STEP 6: RETURN PREDICTION
┌──────────────────────────────────┐
│  {                               │
│    "prediction": 4600,           │
│    "historicalData": [...]       │
│  }                               │
└──────────────────────────────────┘
```

### 8.2 Mathematical Model

```
Linear Regression Formula:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

y = β₀ + β₁x + ε

Where:
  y  = Predicted water usage (liters)
  x  = Day number (0, 1, 2, 3, ...)
  β₀ = Intercept (baseline usage)
  β₁ = Slope (daily trend)
  ε  = Error term

Example Calculation:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Given data:
  Day 0: 5200L
  Day 1: 5400L
  Day 2: 5000L
  Day 3: 4800L

Model learns:
  β₀ = 5300 (average baseline)
  β₁ = -100 (decreasing trend)

Prediction for Day 4:
  y = 5300 + (-100 × 4)
  y = 5300 - 400
  y = 4900 liters
```

### 8.3 Anomaly Detection Algorithm

```
┌─────────────────────────────────────────────────────────────┐
│              ABNORMAL USAGE DETECTION                        │
└─────────────────────────────────────────────────────────────┘

STEP 1: Calculate Average Usage
┌──────────────────────────────────┐
│  total_usage = Σ(all waterUsed)  │
│  count = number of entries       │
│  avg_usage = total / count       │
│                                  │
│  Example:                        │
│  total = 15600                   │
│  count = 12                      │
│  avg = 1300 liters               │
└──────────────────────────────────┘
            ↓
STEP 2: Define Threshold
┌──────────────────────────────────┐
│  threshold = avg_usage × 1.4     │
│  (40% above average)             │
│                                  │
│  Example:                        │
│  threshold = 1300 × 1.4          │
│  threshold = 1820 liters         │
└──────────────────────────────────┘
            ↓
STEP 3: Check Each Entry
┌──────────────────────────────────┐
│  for each entry:                 │
│    if entry.waterUsed > threshold│
│      flag as ABNORMAL            │
│                                  │
│  Example:                        │
│  Entry: 2100L > 1820L            │
│  Result: ABNORMAL ⚠️             │
└──────────────────────────────────┘
            ↓
STEP 4: Alert Generation
┌──────────────────────────────────┐
│  if abnormal detected:           │
│    display alert message         │
│    add to suggestions            │
│                                  │
│  "Possible water leakage or      │
│   abnormal usage detected"       │
└──────────────────────────────────┘
```

## 9. Component Interaction Matrix

```
┌────────────────────────────────────────────────────────────────┐
│              COMPONENT INTERACTION MATRIX                       │
├────────────┬───────────┬──────────┬──────────┬─────────────────┤
│ Component  │ Interacts │ Method   │ Data     │ Purpose         │
│            │ With      │          │ Format   │                 │
├────────────┼───────────┼──────────┼──────────┼─────────────────┤
│ form.html  │ script.js │ Event    │ Form     │ Capture input   │
│            │           │ Listener │ Data     │                 │
├────────────┼───────────┼──────────┼──────────┼─────────────────┤
│ script.js  │ Flask API │ POST     │ JSON     │ Submit data     │
│            │           │ Request  │          │                 │
├────────────┼───────────┼──────────┼──────────┼─────────────────┤
│ Flask API  │ JSON File │ File I/O │ JSON     │ Store data      │
│            │           │          │ Array    │                 │
├────────────┼───────────┼──────────┼──────────┼─────────────────┤
│ dashboard  │ Flask API │ GET      │ JSON     │ Fetch analytics │
│ .html      │           │ Request  │ Response │                 │
├────────────┼───────────┼──────────┼──────────┼─────────────────┤
│ Chart.js   │ dashboard │ JS       │ Arrays   │ Render graphs   │
│            │ .html     │ Function │          │                 │
├────────────┼───────────┼──────────┼──────────┼─────────────────┤
│ prediction │ Flask API │ GET      │ JSON     │ Fetch prediction│
│ .html      │           │ Request  │ Response │                 │
├────────────┼───────────┼──────────┼──────────┼─────────────────┤
│ sklearn    │ Flask API │ Python   │ NumPy    │ ML prediction   │
│            │           │ Import   │ Arrays   │                 │
└────────────┴───────────┴──────────┴──────────┴─────────────────┘
```

## 10. State Management

### 10.1 Application State Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    APPLICATION STATES                        │
└─────────────────────────────────────────────────────────────┘

STATE 1: INITIAL (No Data)
┌──────────────────────────────────┐
│  • JSON file empty or missing    │
│  • Dashboard shows "No data"     │
│  • Prediction unavailable        │
│  • User must enter data first    │
└──────────────────────────────────┘
            ↓ (User enters data)
            
STATE 2: PARTIAL DATA (1-2 entries)
┌──────────────────────────────────┐
│  • JSON has some entries         │
│  • Dashboard shows basic stats   │
│  • Charts display limited data   │
│  • Prediction needs more data    │
└──────────────────────────────────┘
            ↓ (User enters more data)
            
STATE 3: SUFFICIENT DATA (3+ entries)
┌──────────────────────────────────┐
│  • JSON has multiple entries     │
│  • Dashboard fully functional    │
│  • All charts populated          │
│  • Prediction available          │
│  • Anomaly detection active      │
└──────────────────────────────────┘
            ↓ (Continuous usage)
            
STATE 4: RICH DATA (10+ entries)
┌──────────────────────────────────┐
│  • Comprehensive analytics       │
│  • Accurate predictions          │
│  • Trend analysis available      │
│  • Pattern recognition improved  │
└──────────────────────────────────┘
```

### 10.2 Session Flow

```
USER SESSION LIFECYCLE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. User Opens Browser
   └─→ Navigate to localhost:5000
   
2. Flask Server Starts
   └─→ Load routes and initialize app
   
3. Home Page Loads
   └─→ Display navigation options
   
4. User Interaction Loop:
   ┌─────────────────────────────────┐
   │  ┌─→ Enter Data                 │
   │  │   └─→ Submit to API          │
   │  │       └─→ Store in JSON      │
   │  │                              │
   │  ├─→ View Dashboard             │
   │  │   └─→ Fetch analytics        │
   │  │       └─→ Render charts      │
   │  │                              │
   │  ├─→ Check Prediction           │
   │  │   └─→ Run ML model           │
   │  │       └─→ Display forecast   │
   │  │                              │
   │  └─→ Navigate between pages     │
   │      └─→ Repeat cycle           │
   └─────────────────────────────────┘
   
5. User Closes Browser
   └─→ Data persists in JSON file
   
6. Next Session
   └─→ Data loads from JSON
       └─→ Continue from last state
```

## 11. Error Handling Strategy

```
┌─────────────────────────────────────────────────────────────┐
│                    ERROR HANDLING FLOW                       │
└─────────────────────────────────────────────────────────────┘

CLIENT-SIDE VALIDATION (JavaScript)
┌──────────────────────────────────┐
│  • Empty fields                  │
│  • Invalid numbers               │
│  • Current > Previous level      │
│  • Level > Tank capacity         │
│  └─→ Show error message          │
│      └─→ Prevent submission      │
└──────────────────────────────────┘

SERVER-SIDE VALIDATION (Flask)
┌──────────────────────────────────┐
│  • Missing required fields       │
│  • Invalid data types            │
│  • Business logic violations     │
│  └─→ Return error response       │
│      └─→ HTTP 400 Bad Request    │
└──────────────────────────────────┘

FILE OPERATIONS
┌──────────────────────────────────┐
│  • File not found                │
│  • Permission denied             │
│  • Corrupted JSON                │
│  └─→ Create new file             │
│      └─→ Initialize empty array  │
└──────────────────────────────────┘

ML PREDICTION
┌──────────────────────────────────┐
│  • Insufficient data (<3 points) │
│  • Invalid data format           │
│  • Model training failure        │
│  └─→ Return error message        │
│      └─→ Request more data       │
└──────────────────────────────────┘
```

## 12. Performance Considerations

### 12.1 Optimization Strategies

```
DATA LOADING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Load JSON once per request
• Cache in memory during processing
• Avoid multiple file reads

CHART RENDERING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Use Chart.js lazy loading
• Limit data points displayed
• Destroy old charts before creating new

ML PREDICTION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Train model on-demand
• Use simple Linear Regression
• Limit historical data processed

FILE OPERATIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
• Append-only writes
• Atomic file operations
• JSON formatting for readability
```

### 12.2 Scalability Path

```
CURRENT: JSON File Storage
    ↓
PHASE 1: Add Database (Supabase)
    ↓
PHASE 2: Add Caching (Redis)
    ↓
PHASE 3: Add Queue System (Celery)
    ↓
PHASE 4: Microservices Architecture
```

## 13. Security Considerations

```
INPUT VALIDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Validate all user inputs
✓ Sanitize data before storage
✓ Type checking on server side
✓ Range validation for numbers

DATA STORAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ Store in secure directory
✓ Limit file permissions
✓ No sensitive data stored
✓ Regular backups recommended

API SECURITY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✓ CORS configuration
✓ Rate limiting (future)
✓ Input sanitization
✓ Error message sanitization
```

---

## 14. Summary

This Water Usage Analysis System demonstrates a complete full-stack architecture with:

- **Frontend**: Responsive UI with real-time data visualization
- **Backend**: RESTful API with Flask
- **Data Layer**: JSON-based persistence
- **ML Layer**: Predictive analytics using Linear Regression
- **Analytics**: Real-time insights and anomaly detection

The system is designed for easy deployment, minimal dependencies, and future scalability to database-backed solutions.

