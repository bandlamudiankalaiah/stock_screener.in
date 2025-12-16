# 📈 Stock Screener - Complete Project Documentation

## 📋 Table of Contents
1. [Project Overview](#project-overview)
2. [Installation Guide](#installation-guide)
3. [Running the Application](#running-the-application)
4. [Features Explanation](#features-explanation)
5. [Technical Architecture](#technical-architecture)
6. [File Structure](#file-structure)
7. [Database Schema](#database-schema)
8. [API Documentation](#api-documentation)
9. [Troubleshooting](#troubleshooting)

---

## 🎯 Project Overview

**Project Name**: Stock Screener  
**Type**: Web Application  
**Purpose**: Stock analysis and screening tool for investors in India  
**Technology Stack**: Flask (Python), SQLite, JavaScript, CSS  

### What This Application Does:
- Analyzes 100+ Indian stocks with financial metrics
- Allows custom screening based on P/E, ROE, Market Cap, etc.
- Provides company-wise detailed analysis
- Exports filtered data to CSV
- Dark/Light theme support

---

## 🚀 Installation Guide

### Prerequisites
```bash
# Check Python version (Required: 3.8+)
python --version
```

### Step 1: Install Dependencies
```bash
# Install all required packages
pip install -r requirements.txt
```

**What gets installed:**
- Flask 3.0.0 (Web framework)
- Flask-SQLAlchemy 3.1.1 (Database ORM)
- pandas 2.1.4 (Data processing)

### Step 2: Generate Sample Data
```bash
# Create database with 100 sample stocks
python data_generator.py
```

**Output:**
```
Generated 100 stocks with financial metrics
Saved to instance/sample_data.db
```

---

## 🎮 Running the Application

### Start the Server
```bash
# Run the Flask application
python app.py
```

**Expected Output:**
```
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### Access the Application
```
Open browser: http://127.0.0.1:5000
or
Open browser: http://localhost:5000
```

### Stop the Server
```
Press CTRL+C in the terminal
```

---

## 📊 Features Explanation

### 1. **Dashboard** (Home Page)

**URL**: `http://127.0.0.1:5000/`

**What You See:**
- Search bar at the top
- Quick analyze company chips
- Sector filter dropdown
- Stock table with 20 stocks
- Export CSV button

**How to Use:**
1. Browse stocks in the table
2. Click "Analyze" to see company details
3. Use sector dropdown to filter
4. Click "Export CSV" to download data

---

### 2. **Company Search**

**Location**: Top of dashboard

**How It Works:**
1. Type company name or symbol
2. Results appear in dropdown
3. Click any result to view details

**Example Commands to Test:**
```bash
# Search these companies:
- Type: "RELIANCE" → Shows Reliance Industries
- Type: "TCS" → Shows Tata Consultancy Services
- Type: "HDFC" → Shows HDFC Bank
- Type: "INFO" → Shows Infosys
```

---

### 3. **Quick Analyze**

**Location**: Below search bar

**Featured Companies:**
- Reliance Industries
- TCS
- HDFC Bank
- Infosys
- Hindustan Unilever
- ICICI Bank
- SBI
- Bharti Airtel
- ITC
- Wipro
- And more...

**How to Use:**
1. Click any company chip
2. Opens detailed analysis page

---

### 4. **Company Detail Page**

**URL Pattern**: `http://127.0.0.1:5000/company/SYMBOL`

**Examples:**
```
http://127.0.0.1:5000/company/RELIANCE
http://127.0.0.1:5000/company/TCS
http://127.0.0.1:5000/company/HDFCBANK
```

**Information Displayed:**
- Company name and symbol
- Current stock price
- Market capitalization
- 12 key financial metrics
- Quick analysis with indicators

**Metrics Shown:**
1. Market Cap (₹ Cr)
2. P/E Ratio
3. P/B Ratio
4. ROE %
5. ROCE %
6. Debt to Equity
7. EPS (₹)
8. Revenue Growth %
9. Profit Growth %
10. Dividend Yield %
11. Promoter Holding %
12. Current Ratio

---

### 5. **Create Custom Screen**

**URL**: `http://127.0.0.1:5000/screen/create`

**Step-by-Step:**

1. **Enter Screen Name**
   ```
   Example: "Value Stocks"
   ```

2. **Add Filter Criteria**
   - Click "+ Add Filter"
   - Select metric (e.g., P/E Ratio)
   - Choose operator (>, <, =, between)
   - Enter value (e.g., 15)

3. **Test Screen**
   - Click "Test Screen" button
   - See matching stocks

4. **Save Screen**
   - Click "Save Screen" button
   - Screen saved for future use

**Example Screens:**

**Screen 1: Value Stocks**
```
Name: Value Stocks
Criteria:
  - P/E Ratio < 15
  - ROE % > 15
  - Debt to Equity < 1
```

**Screen 2: Growth Stocks**
```
Name: Growth Stocks
Criteria:
  - Revenue Growth % > 20
  - Profit Growth % > 15
  - ROE % > 20
```

**Screen 3: High Dividend**
```
Name: High Dividend Stocks
Criteria:
  - Dividend Yield % > 3
  - Promoter Holding % > 50
  - Debt to Equity < 1.5
```

**Screen 4: Banking Sector**
```
Name: Banking Analysis
Criteria:
  - Sector = Banking
  - Market Cap > 10000
  - ROE % > 12
```

---

### 6. **My Screens**

**How to Access:**
1. Click "My Screens" button in navbar
2. Modal opens with saved screens

**Actions Available:**
- **Apply**: Run the screen filter
- **Edit**: Modify criteria
- **Delete**: Remove screen

---

### 7. **Theme Switcher**

**Location**: Top-right navbar (🌓 button)

**How to Use:**
1. Click 🌓 button
2. Theme toggles between Light/Dark
3. Preference saved in browser

**Themes:**
- ☀️ Light Theme (Default)
- 🌙 Dark Theme

---

### 8. **Export to CSV**

**Location**: Dashboard

**How to Export:**
1. (Optional) Apply filters
2. Click "📥 Export CSV" button
3. File downloads automatically

**File Format:**
```
stock_screener_2025-12-16.csv
```

**Columns Included:**
- Symbol
- Name
- Sector
- Market Cap
- Price
- P/E
- P/B
- ROE%
- ROCE%
- Debt/Eq

---

## 🏗️ Technical Architecture

### Backend (Python/Flask)

**Main Files:**
1. `app.py` - Flask application with routes
2. `database.py` - Database models
3. `data_generator.py` - Sample data generator

**Routes:**
```python
GET  /                          # Dashboard
GET  /company/<symbol>          # Company details
GET  /screen/create             # Create screen page
GET  /screen/<id>/edit          # Edit screen page
DELETE /screen/<id>/delete      # Delete screen
GET  /screens                   # List all screens
GET  /api/search?q=<query>      # Search stocks
POST /api/stocks/filter         # Filter stocks
POST /api/export                # Export CSV
```

### Frontend (HTML/CSS/JS)

**Templates:**
1. `index.html` - Dashboard page
2. `company.html` - Company detail page
3. `screen.html` - Screen builder page

**Static Files:**
1. `style.css` - All styling
2. `main.js` - JavaScript functionality

### Database (SQLite)

**Location**: `instance/sample_data.db`

**Tables:**
1. `stocks` - Stock data (100 records)
2. `screens` - Saved screens

---

## 📁 File Structure

```
screener.in3/
├── app.py                      # Main Flask application
├── database.py                 # Database models (Stock, Screen)
├── data_generator.py           # Sample data generator
├── test_app.py                 # Test script
├── requirements.txt            # Python dependencies
├── README.md                   # Quick start guide
├── COMMANDS.md                 # Command reference
├── FEATURES.md                 # Feature documentation
├── PROJECT_DOCUMENTATION.md    # This file
│
├── templates/                  # HTML templates
│   ├── index.html             # Dashboard
│   ├── company.html           # Company details
│   └── screen.html            # Screen builder
│
├── static/                     # Static assets
│   ├── css/
│   │   └── style.css          # All styles
│   └── js/
│       └── main.js            # JavaScript
│
└── instance/                   # Database folder
    └── sample_data.db         # SQLite database
```

---

## 🗄️ Database Schema

### Table: `stocks`

| Column | Type | Description |
|--------|------|-------------|
| symbol | String(20) | Stock symbol (Primary Key) |
| name | String(100) | Company name |
| sector | String(50) | Industry sector |
| market_cap | Float | Market cap in crores |
| current_price | Float | Stock price in ₹ |
| pe_ratio | Float | Price to Earnings ratio |
| pb_ratio | Float | Price to Book ratio |
| roe | Float | Return on Equity % |
| roce | Float | Return on Capital % |
| debt_to_equity | Float | Debt to Equity ratio |
| eps | Float | Earnings per share |
| revenue_growth | Float | Revenue growth % |
| profit_growth | Float | Profit growth % |
| dividend_yield | Float | Dividend yield % |
| promoter_holding | Float | Promoter holding % |
| price_to_sales | Float | Price to Sales ratio |
| current_ratio | Float | Current ratio |
| last_updated | String(20) | Last update date |

### Table: `screens`

| Column | Type | Description |
|--------|------|-------------|
| id | Integer | Screen ID (Primary Key) |
| name | String(100) | Screen name |
| criteria | Text | JSON string of criteria |
| created_at | DateTime | Creation timestamp |
| updated_at | DateTime | Update timestamp |

---

## 🔌 API Documentation

### 1. Search Stocks
```http
GET /api/search?q=<query>
```

**Example:**
```bash
curl "http://127.0.0.1:5000/api/search?q=RELIANCE"
```

**Response:**
```json
[
  {
    "symbol": "RELIANCE",
    "name": "Reliance Industries",
    "sector": "Energy",
    "current_price": 160.2,
    "market_cap": 143800
  }
]
```

### 2. Filter Stocks
```http
POST /api/stocks/filter
Content-Type: application/json

{
  "criteria": [
    {
      "metric": "roe",
      "operator": "greater_than",
      "value": "15"
    }
  ]
}
```

**Example:**
```bash
curl -X POST http://127.0.0.1:5000/api/stocks/filter \
  -H "Content-Type: application/json" \
  -d '{"criteria":[{"metric":"roe","operator":"greater_than","value":"15"}]}'
```

### 3. Export CSV
```http
POST /api/export
Content-Type: application/json

{
  "criteria": []
}
```

---

## 🛠️ Troubleshooting

### Issue 1: Port Already in Use

**Error:**
```
Address already in use
```

**Solution (Windows):**
```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace 1234 with actual PID)
taskkill /PID 1234 /F
```

**Solution (Linux/Mac):**
```bash
# Kill process on port 5000
lsof -ti:5000 | xargs kill -9
```

### Issue 2: Database Not Found

**Error:**
```
No such file or directory: instance/sample_data.db
```

**Solution:**
```bash
# Regenerate database
python data_generator.py
```

### Issue 3: Module Not Found

**Error:**
```
ModuleNotFoundError: No module named 'flask'
```

**Solution:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Issue 4: Empty Database

**Check:**
```bash
# Verify stock count
python -c "from database import db, Stock; from app import app; app.app_context().push(); print(f'Stocks: {Stock.query.count()}')"
```

**Solution:**
```bash
# Regenerate data
python data_generator.py
```

---

## 📝 Testing Commands

### Test 1: Verify Installation
```bash
python --version
pip list | findstr Flask
```

### Test 2: Check Database
```bash
python test_app.py
```

### Test 3: Test Routes
```bash
# Test search API
curl "http://127.0.0.1:5000/api/search?q=TCS"

# Test filter API
curl -X POST http://127.0.0.1:5000/api/stocks/filter -H "Content-Type: application/json" -d "{\"criteria\":[]}"
```

---

## 🎓 How to Explain to Others

### Quick Demo Script:

**1. Introduction (30 seconds)**
```
"This is a Stock Screener application built with Flask and Python.
It helps investors analyze and filter Indian stocks based on
financial metrics like P/E ratio, ROE, Market Cap, etc."
```

**2. Show Dashboard (1 minute)**
```
"Here's the main dashboard showing 100 stocks.
You can see key metrics like Market Cap, Price, ROE, ROCE.
Green values indicate good performance, red indicates poor."
```

**3. Demo Search (30 seconds)**
```
"Let me search for a company... typing 'RELIANCE'...
and here are the results. Click to see detailed analysis."
```

**4. Show Company Details (1 minute)**
```
"This page shows complete financial analysis of Reliance Industries.
We have 12 key metrics, current price, and quick indicators
showing if the company has strong ROE, low debt, good growth, etc."
```

**5. Demo Screening (2 minutes)**
```
"Now let's create a custom screen for Value Stocks.
I'll add filters: P/E less than 15, ROE greater than 15,
and Debt to Equity less than 1.
Click Test Screen... and here are 15 stocks matching our criteria.
Let's save this screen for future use."
```

**6. Show Theme Toggle (15 seconds)**
```
"The app supports dark mode. Click this button...
and the entire theme changes. Very easy on the eyes."
```

**7. Demo Export (15 seconds)**
```
"Finally, you can export any filtered data to CSV.
Click Export... and the file downloads immediately."
```

---

## 📊 Presentation Slides Outline

### Slide 1: Title
- Stock Screener
- Stock Analysis Tool for Indian Investors
- Built with Flask & Python

### Slide 2: Problem Statement
- Investors need to analyze hundreds of stocks
- Manual analysis is time-consuming
- Need custom filtering based on criteria

### Slide 3: Solution
- Web-based stock screener
- 100+ Indian stocks
- 15 financial metrics
- Custom screening capability

### Slide 4: Key Features
1. Real-time company search
2. Detailed company analysis
3. Custom stock screening
4. Save & manage screens
5. Export to CSV
6. Dark/Light themes

### Slide 5: Technology Stack
- Backend: Flask (Python)
- Database: SQLite
- Frontend: HTML, CSS, JavaScript
- No external dependencies

### Slide 6: Database
- 100 stocks
- 10 sectors
- 15 metrics per stock
- Real-time filtering

### Slide 7: Demo Screenshots
- Dashboard
- Company Detail Page
- Screen Builder
- Theme Toggle

### Slide 8: Use Cases
- Value investing
- Growth stock hunting
- Sector analysis
- Portfolio screening

### Slide 9: Future Enhancements
- Real-time stock data API
- More metrics
- Charting capabilities
- Portfolio tracking

### Slide 10: Conclusion
- Fully functional
- Easy to use
- Scalable architecture
- Open for enhancements

---

## 🎯 Quick Commands Cheat Sheet

```bash
# Installation
pip install -r requirements.txt

# Generate Data
python data_generator.py

# Run Application
python app.py

# Test Application
python test_app.py

# Check Database
python -c "from database import db, Stock; from app import app; app.app_context().push(); print(Stock.query.count())"

# Access Application
# Open: http://127.0.0.1:5000

# Stop Server
# Press CTRL+C
```

---

**Document Version**: 1.0  
**Last Updated**: 2025-12-16  
**Status**: ✅ Complete & Verified