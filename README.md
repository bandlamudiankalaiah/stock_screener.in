# 📈 Stock Screener Application

A Flask-based web application for screening Indian stocks based on various financial metrics like P/E ratio, ROE, ROCE, Market Cap, and more.

## 🎯 Features

- **Stock Universe**: View 100+ Indian stocks with real-time financial metrics
- **Custom Screening**: Create custom filters based on multiple criteria
- **Save Screens**: Save your favorite screening strategies
- **Quick Filters**: Filter by sector with one click
- **Export Data**: Download filtered results as CSV
- **No Login Required**: Direct access to dashboard

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## 🚀 Installation & Setup

### Step 1: Install Dependencies

Open your terminal/command prompt in the project directory and run:

```bash
pip install -r requirements.txt
```

This will install:
- Flask (Web framework)
- Flask-SQLAlchemy (Database ORM)
- pandas (Data manipulation)

### Step 2: Generate Sample Data (Optional)

If you want to populate the database with fresh sample data:

```bash
python data_generator.py
```

This creates 100 sample stocks with realistic financial metrics in `instance/sample_data.db`

### Step 3: Run the Application

```bash
python app.py
```

You should see output like:
```
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000
```

### Step 4: Access the Application

Open your web browser and go to:
```
http://127.0.0.1:5000
```

or

```
http://localhost:5000
```

## 🛑 Stopping the Server

Press `CTRL+C` in the terminal where the Flask app is running.

## 📊 How to Use

### 1. Dashboard
- View all stocks in a table format
- See key metrics: Market Cap, Price, P/E, P/B, ROE, ROCE, etc.
- Use the sector dropdown for quick filtering

### 2. Create Custom Screen
- Click **"+ Create New Screen"** button
- Add multiple filter criteria:
  - Select metric (e.g., ROE, P/E Ratio, Market Cap)
  - Choose operator (>, <, =, between)
  - Enter value
- Click **"Test Screen"** to preview results
- Click **"Save Screen"** to save for later use

### 3. Manage Saved Screens
- Click **"My Screens"** to view all saved screens
- **Apply**: Run the screen and see filtered results
- **Edit**: Modify screening criteria
- **Delete**: Remove unwanted screens

### 4. Export Data
- Click **"Export CSV"** to download current results
- File will be saved as `stock_screener_YYYY-MM-DD.csv`

## 📁 Project Structure

```
screener.in3/
├── app.py                      # Main Flask application
├── database.py                 # Database models (Stock, Screen)
├── data_generator.py           # Sample data generator
├── requirements.txt            # Python dependencies
├── README.md                   # This file
│
├── templates/                  # HTML templates
│   ├── index.html             # Dashboard page
│   └── screen.html            # Screen builder page
│
├── static/                     # Static assets
│   ├── css/
│   │   └── style.css          # Stylesheet
│   └── js/
│       └── main.js            # JavaScript functionality
│
└── instance/                   # Database folder (auto-created)
    └── sample_data.db         # SQLite database
```

## 🔧 Available Screening Metrics

| Metric | Description | Type |
|--------|-------------|------|
| Market Cap | Market Capitalization (₹ Cr) | Number |
| Current Price | Stock Price (₹) | Number |
| P/E Ratio | Price to Earnings Ratio | Number |
| P/B Ratio | Price to Book Ratio | Number |
| ROE % | Return on Equity | Percentage |
| ROCE % | Return on Capital Employed | Percentage |
| Debt to Equity | Debt to Equity Ratio | Number |
| EPS | Earnings Per Share (₹) | Number |
| Revenue Growth % | Year-over-Year Revenue Growth | Percentage |
| Profit Growth % | Year-over-Year Profit Growth | Percentage |
| Dividend Yield % | Dividend Yield | Percentage |
| Promoter Holding % | Promoter Shareholding | Percentage |
| Price to Sales | Price to Sales Ratio | Number |
| Current Ratio | Current Assets / Current Liabilities | Number |
| Sector | Industry Sector | Text |

## 💡 Example Screening Strategies

### Value Stocks
```
P/E Ratio < 15
ROE % > 15
Debt to Equity < 1
```

### Growth Stocks
```
Revenue Growth % > 20
Profit Growth % > 15
ROE % > 20
```

### High Dividend Stocks
```
Dividend Yield % > 3
Promoter Holding % > 50
Debt to Equity < 1.5
```

### Banking Sector Analysis
```
Sector = Banking
Market Cap > 10000
ROE % > 12
```

## 🐛 Troubleshooting

### Port Already in Use
If you see "Address already in use" error:

**Windows:**
```powershell
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (replace PID with actual process ID)
taskkill /PID <PID> /F
```

**Linux/Mac:**
```bash
# Find and kill process
lsof -ti:5000 | xargs kill -9
```

### Database Not Found
If you get database errors, regenerate the database:
```bash
python data_generator.py
```

### Module Not Found Error
Reinstall dependencies:
```bash
pip install -r requirements.txt --force-reinstall
```

## 📝 Technical Details

- **Backend**: Flask 3.0.0
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: Vanilla JavaScript + CSS
- **Data Processing**: pandas
- **Server**: Flask Development Server (Debug Mode)

## ⚠️ Important Notes

1. This is a **development server** - not suitable for production
2. Database is SQLite - for demo purposes only
3. Stock data is **randomly generated** - not real market data
4. No authentication required - direct access to all features

## 🔄 Updating Stock Data

To refresh the database with new random data:

```bash
python data_generator.py
```

Then restart the Flask server:
```bash
python app.py
```

## 📧 Support

For issues or questions about running the application, check:
1. All dependencies are installed (`pip list`)
2. Python version is 3.8+ (`python --version`)
3. Port 5000 is available
4. Database file exists in `instance/` folder

---

**Happy Stock Screening! 📊📈**