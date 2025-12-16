# 🚀 Quick Command Reference

## Essential Commands

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
**What it does**: Installs Flask, Flask-SQLAlchemy, and pandas

---

### 2️⃣ Generate Sample Data (Optional)
```bash
python data_generator.py
```
**What it does**: Creates 100 sample stocks in the database
**Output**: `Generated 100 stocks with financial metrics`

---

### 3️⃣ Run the Application
```bash
python app.py
```
**What it does**: Starts the Flask web server
**Expected Output**:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

---

### 4️⃣ Stop the Server
```
Press CTRL+C
```
**What it does**: Stops the Flask server

---

## Troubleshooting Commands

### Check Python Version
```bash
python --version
```
**Required**: Python 3.8 or higher

---

### Check Installed Packages
```bash
pip list
```
**Look for**: Flask, Flask-SQLAlchemy, pandas

---

### Reinstall Dependencies
```bash
pip install -r requirements.txt --force-reinstall
```
**When to use**: If packages are corrupted or missing

---

### Kill Process on Port 5000 (Windows)
```powershell
# Find process
netstat -ano | findstr :5000

# Kill process (replace 1234 with actual PID)
taskkill /PID 1234 /F
```

---

### Kill Process on Port 5000 (Linux/Mac)
```bash
lsof -ti:5000 | xargs kill -9
```

---

## File Operations

### List Project Files
```bash
# Windows
dir /s /b

# Linux/Mac
ls -R
```

---

### Check Database Exists
```bash
# Windows
dir instance\sample_data.db

# Linux/Mac
ls -l instance/sample_data.db
```

---

### Delete Database (Fresh Start)
```bash
# Windows
del instance\sample_data.db

# Linux/Mac
rm instance/sample_data.db
```
**Then run**: `python data_generator.py` to recreate

---

## Development Commands

### Run with Specific Port
```bash
# Edit app.py, change last line to:
app.run(debug=True, port=8000)
```

---

### Run without Debug Mode
```bash
# Edit app.py, change last line to:
app.run(debug=False, port=5000)
```

---

## Access URLs

- **Dashboard**: http://127.0.0.1:5000
- **Alternative**: http://localhost:5000
- **Create Screen**: http://127.0.0.1:5000/screen/create

---

## Complete Workflow

```bash
# Step 1: Install
pip install -r requirements.txt

# Step 2: Generate data (optional)
python data_generator.py

# Step 3: Run server
python app.py

# Step 4: Open browser
# Go to http://127.0.0.1:5000

# Step 5: Stop server when done
# Press CTRL+C
```

---

## Quick Checks

### ✅ Everything Working?
1. No error messages when running `python app.py`
2. See "Running on http://127.0.0.1:5000" message
3. Browser opens the dashboard successfully
4. Can see stock data in the table

### ❌ Something Wrong?
1. Check Python version: `python --version`
2. Reinstall packages: `pip install -r requirements.txt`
3. Regenerate database: `python data_generator.py`
4. Check port 5000 is free
5. Restart terminal/command prompt

---

**Need Help?** Check README.md for detailed explanations!