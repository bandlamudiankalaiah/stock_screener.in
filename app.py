from flask import Flask, render_template, jsonify, request, session, redirect, url_for, Response
from database import db, Stock, Screen, init_db
import json
import os

app = Flask(__name__)
app.secret_key = "your-secret-key-for-final-year-project"

# Ensure instance path exists
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'instance', 'sample_data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

# Available metrics for screening
METRICS = {
    "market_cap": {"type": "number", "label": "Market Cap (Cr)", "unit": "₹ Cr"},
    "current_price": {"type": "number", "label": "Current Price", "unit": "₹"},
    "pe_ratio": {"type": "number", "label": "P/E Ratio"},
    "pb_ratio": {"type": "number", "label": "P/B Ratio"},
    "roe": {"type": "percentage", "label": "ROE %", "unit": "%"},
    "roce": {"type": "percentage", "label": "ROCE %", "unit": "%"},
    "debt_to_equity": {"type": "number", "label": "Debt to Equity"},
    "eps": {"type": "number", "label": "EPS", "unit": "₹"},
    "revenue_growth": {"type": "percentage", "label": "Revenue Growth %", "unit": "%"},
    "profit_growth": {"type": "percentage", "label": "Profit Growth %", "unit": "%"},
    "dividend_yield": {"type": "percentage", "label": "Dividend Yield %", "unit": "%"},
    "promoter_holding": {"type": "percentage", "label": "Promoter Holding %", "unit": "%"},
    "price_to_sales": {"type": "number", "label": "Price to Sales"},
    "current_ratio": {"type": "number", "label": "Current Ratio"},
    "sector": {"type": "string", "label": "Sector"}
}

@app.route('/')
def dashboard():
    # Get all stocks for initial display
    stocks = Stock.query.limit(20).all()
    sectors = [s[0] for s in db.session.query(Stock.sector).distinct().all()]
    # Get some featured companies for quick analyze
    featured = Stock.query.limit(12).all()
    return render_template('index.html', stocks=stocks, sectors=sectors, metrics=METRICS, featured=featured)

@app.route('/api/search', methods=['GET'])
def search_stocks():
    query = request.args.get('q', '').strip()
    if not query:
        return jsonify([])
    
    # Search by symbol or name
    stocks = Stock.query.filter(
        db.or_(
            Stock.symbol.ilike(f'%{query}%'),
            Stock.name.ilike(f'%{query}%')
        )
    ).limit(10).all()
    
    return jsonify([{
        "symbol": s.symbol,
        "name": s.name,
        "sector": s.sector,
        "current_price": s.current_price,
        "market_cap": s.market_cap
    } for s in stocks])

@app.route('/company/<symbol>')
def company_detail(symbol):
    stock = Stock.query.filter_by(symbol=symbol).first_or_404()
    return render_template('company.html', stock=stock, metrics=METRICS)

@app.route('/screens')
def screens():
    screens = Screen.query.order_by(Screen.updated_at.desc()).all()
    return jsonify([{
        "id": s.id,
        "name": s.name,
        "criteria": json.loads(s.criteria),
        "created_at": s.created_at.isoformat(),
        "updated_at": s.updated_at.isoformat()
    } for s in screens])

@app.route('/screen/create', methods=['GET', 'POST'])
def create_screen():
    if request.method == 'POST':
        data = request.json
        screen = Screen(
            name=data['name'],
            criteria=json.dumps(data['criteria'])
        )
        db.session.add(screen)
        db.session.commit()
        return jsonify({"success": True, "id": screen.id})
    
    return render_template('screen.html', metrics=METRICS, mode='create', screen_data=None)

@app.route('/screen/<int:screen_id>/edit', methods=['GET', 'PUT'])
def edit_screen(screen_id):
    screen = Screen.query.get_or_404(screen_id)
    
    if request.method == 'PUT':
        data = request.json
        screen.name = data['name']
        screen.criteria = json.dumps(data['criteria'])
        db.session.commit()
        return jsonify({"success": True})
    
    return render_template('screen.html', metrics=METRICS, mode='edit', 
                         screen_data={"id": screen.id, "name": screen.name, 
                                    "criteria": json.loads(screen.criteria)})

@app.route('/screen/<int:screen_id>/delete', methods=['DELETE'])
def delete_screen(screen_id):
    screen = Screen.query.get_or_404(screen_id)
    db.session.delete(screen)
    db.session.commit()
    return jsonify({"success": True})

@app.route('/api/stocks/filter', methods=['POST'])
def filter_stocks():
    criteria = request.json.get('criteria', [])
    
    # Build SQL query dynamically
    query = Stock.query
    
    for criterion in criteria:
        metric = criterion['metric']
        operator = criterion['operator']
        value = criterion['value']
        
        column = getattr(Stock, metric)
        
        if metric == 'sector':
            if operator == 'equals':
                query = query.filter(column == value)
            elif operator == 'contains':
                query = query.filter(column.contains(value))
        else:
            try:
                if operator == 'greater_than':
                    query = query.filter(column > float(value))
                elif operator == 'less_than':
                    query = query.filter(column < float(value))
                elif operator == 'equals':
                    query = query.filter(column == float(value))
                elif operator == 'between':
                    # Handle range like "10-20"
                    min_val, max_val = map(float, value.split('-'))
                    query = query.filter(column.between(min_val, max_val))
            except ValueError:
                pass
    
    stocks = query.all()
    
    return jsonify([{
        "symbol": s.symbol,
        "name": s.name,
        "sector": s.sector,
        "market_cap": s.market_cap,
        "current_price": s.current_price,
        "pe_ratio": s.pe_ratio,
        "pb_ratio": s.pb_ratio,
        "roe": s.roe,
        "roce": s.roce,
        "debt_to_equity": s.debt_to_equity,
        "eps": s.eps,
        "revenue_growth": s.revenue_growth,
        "profit_growth": s.profit_growth,
        "dividend_yield": s.dividend_yield,
        "promoter_holding": s.promoter_holding
    } for s in stocks])

@app.route('/api/export', methods=['POST'])
def export_data():
    criteria = request.json.get('criteria', [])
    
    # Apply filters
    query = Stock.query
    for criterion in criteria:
        metric = criterion['metric']
        operator = criterion['operator']
        value = criterion['value']
        column = getattr(Stock, metric)

        if metric == 'sector':
            if operator == 'equals':
                query = query.filter(column == value)
            elif operator == 'contains':
                query = query.filter(column.contains(value))
        else:
            try:
                if operator == 'greater_than':
                    query = query.filter(column > float(value))
                elif operator == 'less_than':
                    query = query.filter(column < float(value))
                elif operator == 'equals':
                    query = query.filter(column == float(value))
                elif operator == 'between':
                    # Handle range like "10-20"
                    min_val, max_val = map(float, value.split('-'))
                    query = query.filter(column.between(min_val, max_val))
            except ValueError:
                pass
    
    stocks = query.all()
    
    # Export to CSV
    import csv
    import io
    output = io.StringIO()
    writer = csv.writer(output)
    
    # Write headers
    headers = ["Symbol", "Name", "Sector", "Market Cap", "Price", "PE", "PB", "ROE%", "ROCE%", "Debt/Eq"]
    writer.writerow(headers)
    
    # Write data
    for s in stocks:
        writer.writerow([
            s.symbol, s.name, s.sector, s.market_cap, s.current_price,
            s.pe_ratio, s.pb_ratio, s.roe, s.roce, s.debt_to_equity
        ])
    
    output.seek(0)
    return Response(output.getvalue(), mimetype='text/csv', headers={"Content-Disposition": "attachment; filename=stocks.csv"})

if __name__ == '__main__':
    # For local development
    app.run(debug=True, port=5000)