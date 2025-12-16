import pandas as pd
import sqlite3
import random
from datetime import datetime
import os

# Sample Indian company data
companies = [
    {"symbol": "RELIANCE", "name": "Reliance Industries", "sector": "Energy"},
    {"symbol": "TCS", "name": "Tata Consultancy Services", "sector": "IT"},
    {"symbol": "HDFCBANK", "name": "HDFC Bank", "sector": "Banking"},
    {"symbol": "INFY", "name": "Infosys", "sector": "IT"},
    {"symbol": "HINDUNILVR", "name": "Hindustan Unilever", "sector": "FMCG"},
    {"symbol": "ICICIBANK", "name": "ICICI Bank", "sector": "Banking"},
    {"symbol": "SBIN", "name": "State Bank of India", "sector": "Banking"},
    {"symbol": "BHARTIARTL", "name": "Bharti Airtel", "sector": "Telecom"},
    {"symbol": "ITC", "name": "ITC Limited", "sector": "FMCG"},
    {"symbol": "WIPRO", "name": "Wipro", "sector": "IT"},
    # Add 90 more companies...
]

# Generate additional companies for a bigger dataset
sectors = ["Energy", "IT", "Banking", "FMCG", "Telecom", "Pharma", "Auto", "Metals", "Cement", "Retail"]
for i in range(90):
    companies.append({
        "symbol": f"COMP{i:03d}",
        "name": f"Company {i} Limited",
        "sector": random.choice(sectors)
    })

# Generate financial metrics
data = []
for company in companies:
    # Realistic ranges for financial metrics
    mcap = random.randint(5000, 150000)  # Market cap in crores
    price = random.uniform(50, 5000)
    pe = random.uniform(5, 80) if random.random() > 0.1 else None  # 10% negative PE
    pb = random.uniform(0.5, 15)
    roe = random.uniform(5, 40)
    roce = random.uniform(8, 45)
    debt_to_equity = random.uniform(0, 3)
    eps = random.uniform(5, 500)
    revenue_growth = random.uniform(-10, 50)
    profit_growth = random.uniform(-20, 60)
    dividend_yield = random.uniform(0, 5)
    promoter_holding = random.uniform(20, 75)
    price_to_sales = random.uniform(1, 12)
    current_ratio = random.uniform(0.8, 4)
    
    data.append({
        "symbol": company["symbol"],
        "name": company["name"],
        "sector": company["sector"],
        "market_cap": mcap,
        "current_price": round(price, 2),
        "pe_ratio": round(pe, 2) if pe else None,
        "pb_ratio": round(pb, 2),
        "roe": round(roe, 2),
        "roce": round(roce, 2),
        "debt_to_equity": round(debt_to_equity, 2),
        "eps": round(eps, 2),
        "revenue_growth": round(revenue_growth, 2),
        "profit_growth": round(profit_growth, 2),
        "dividend_yield": round(dividend_yield, 2),
        "promoter_holding": round(promoter_holding, 2),
        "price_to_sales": round(price_to_sales, 2),
        "current_ratio": round(current_ratio, 2),
        "last_updated": datetime.now().strftime("%Y-%m-%d")
    })

# Create DataFrame and save to SQLite
if not os.path.exists('instance'):
    os.makedirs('instance')

df = pd.DataFrame(data)
conn = sqlite3.connect('instance/sample_data.db')
df.to_sql('stocks', conn, if_exists='replace', index=False)
conn.close()

print(f"Generated {len(data)} stocks with financial metrics")
print(f"Saved to instance/sample_data.db")
