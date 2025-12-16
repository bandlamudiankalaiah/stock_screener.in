# Stock Screener Portal - Final Year Project

## Project Overview
A web-based stock screening tool that allows users to create custom screens using multiple financial filters, similar to Screener.in. Built with Flask, SQLite, and vanilla JavaScript.

## Features Implemented
✅ User Authentication (simplified)  
✅ Dashboard with stock universe  
✅ Custom screen builder with multiple criteria  
✅ Real-time filtering  
✅ Save/load screens  
✅ Export data to CSV  
✅ Responsive UI design  

## Technology Stack
- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite
- **Data**: 100+ Indian stocks with 15+ financial metrics

## Installation & Running
1. Install Python 3.8+
2. `pip install -r requirements.txt`
3. `python data_generator.py` (creates sample data)
4. `python app.py`
5. Open browser to `http://localhost:5000`

## Default Login
- **Email**: student@gmail.com
- **Password**: password123

## Key Algorithms
### Dynamic SQL Query Builder
The system builds SQL queries dynamically based on user-selected filters:
```python
# Example: PE < 20 AND ROE > 15
query = query.filter(Stock.pe_ratio < 20)
query = query.filter(Stock.roe > 15)