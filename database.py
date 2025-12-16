from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Stock(db.Model):
    __tablename__ = 'stocks'
    
    symbol = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sector = db.Column(db.String(50), nullable=False)
    market_cap = db.Column(db.Float, nullable=False)
    current_price = db.Column(db.Float, nullable=False)
    pe_ratio = db.Column(db.Float, nullable=True)
    pb_ratio = db.Column(db.Float, nullable=False)
    roe = db.Column(db.Float, nullable=False)
    roce = db.Column(db.Float, nullable=False)
    debt_to_equity = db.Column(db.Float, nullable=False)
    eps = db.Column(db.Float, nullable=False)
    revenue_growth = db.Column(db.Float, nullable=False)
    profit_growth = db.Column(db.Float, nullable=False)
    dividend_yield = db.Column(db.Float, nullable=False)
    promoter_holding = db.Column(db.Float, nullable=False)
    price_to_sales = db.Column(db.Float, nullable=False)
    current_ratio = db.Column(db.Float, nullable=False)
    last_updated = db.Column(db.String(20), nullable=False)

class Screen(db.Model):
    __tablename__ = 'screens'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    criteria = db.Column(db.Text, nullable=False)  # Store as JSON string
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()