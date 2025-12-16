# 🚀 Deployment Guide - Stock Screener

## 📋 Deployment Options

### Option 1: Render (Recommended)
### Option 2: Heroku
### Option 3: PythonAnywhere
### Option 4: Railway

---

## 🎯 Option 1: Deploy to Render (FREE)

### Step 1: Prepare Your Repository

**Files Required:**
- ✅ `requirements.txt` (with gunicorn)
- ✅ `wsgi.py` (WSGI entry point)
- ✅ `render.yaml` (Render configuration)
- ✅ `runtime.txt` (Python version)

**All files are already created!**

### Step 2: Push to GitHub

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Stock Screener"

# Create GitHub repository and push
git remote add origin https://github.com/YOUR_USERNAME/stock-screener.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy on Render

1. **Go to Render**: https://render.com
2. **Sign up/Login** with GitHub
3. **Click "New +"** → Select "Web Service"
4. **Connect Repository**: Select your stock-screener repo
5. **Configure**:
   - **Name**: `stock-screener`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && python data_generator.py`
   - **Start Command**: `gunicorn wsgi:app`
   - **Instance Type**: `Free`
6. **Click "Create Web Service"**

### Step 4: Wait for Deployment

- Build takes 2-5 minutes
- Render will automatically run the build and start commands
- You'll get a URL like: `https://stock-screener-xxxx.onrender.com`

### ✅ Done! Your app is live!

---

## 🎯 Option 2: Deploy to Heroku

### Step 1: Install Heroku CLI

```bash
# Download from: https://devcenter.heroku.com/articles/heroku-cli
```

### Step 2: Create Procfile

```bash
# Create Procfile (already created for you)
echo "web: gunicorn wsgi:app" > Procfile
```

### Step 3: Deploy

```bash
# Login to Heroku
heroku login

# Create app
heroku create stock-screener-app

# Push to Heroku
git push heroku main

# Run database setup
heroku run python data_generator.py

# Open app
heroku open
```

---

## 🎯 Option 3: Deploy to PythonAnywhere

### Step 1: Sign Up

1. Go to: https://www.pythonanywhere.com
2. Create free account

### Step 2: Upload Code

1. Go to **Files** tab
2. Upload all your project files
3. Or clone from GitHub:
   ```bash
   git clone https://github.com/YOUR_USERNAME/stock-screener.git
   ```

### Step 3: Setup Virtual Environment

```bash
# In Bash console
mkvirtualenv --python=/usr/bin/python3.11 myenv
pip install -r requirements.txt
python data_generator.py
```

### Step 4: Configure Web App

1. Go to **Web** tab
2. Click **Add a new web app**
3. Choose **Manual configuration**
4. Select **Python 3.11**
5. Set **Source code**: `/home/yourusername/stock-screener`
6. Set **WSGI file**: Edit to:

```python
import sys
path = '/home/yourusername/stock-screener'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

7. Click **Reload**

---

## 🎯 Option 4: Deploy to Railway

### Step 1: Sign Up

1. Go to: https://railway.app
2. Sign up with GitHub

### Step 2: Deploy

1. Click **New Project**
2. Select **Deploy from GitHub repo**
3. Choose your repository
4. Railway auto-detects Python
5. Add environment variables if needed
6. Deploy!

---

## 📝 Important Notes for Production

### 1. Change Secret Key

In `app.py`, change:
```python
app.secret_key = "your-secret-key-for-final-year-project"
```

To:
```python
import os
app.secret_key = os.environ.get('SECRET_KEY', 'fallback-secret-key-change-this')
```

### 2. Database Considerations

**Current**: SQLite (good for demo)

**For Production**:
- Use PostgreSQL for better performance
- Add database migrations with Flask-Migrate

### 3. Environment Variables

Create `.env` file (don't commit this):
```
SECRET_KEY=your-super-secret-key-here
DATABASE_URL=sqlite:///instance/sample_data.db
FLASK_ENV=production
```

---

## 🔧 Local Testing Before Deployment

### Test with Gunicorn Locally

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn wsgi:app

# Access at: http://127.0.0.1:8000
```

### Test Production Settings

```bash
# Set environment to production
export FLASK_ENV=production

# Run
python app.py
```

---

## ✅ Deployment Checklist

Before deploying, ensure:

- [ ] `requirements.txt` includes gunicorn
- [ ] `wsgi.py` file exists
- [ ] Database is generated (`python data_generator.py`)
- [ ] Secret key is secure
- [ ] All files are committed to git
- [ ] `.gitignore` excludes sensitive files
- [ ] Tested locally with gunicorn

---

## 🎯 Recommended: Render Deployment

**Why Render?**
- ✅ Free tier available
- ✅ Easy GitHub integration
- ✅ Automatic deployments
- ✅ Free SSL certificate
- ✅ Good performance

**Start Command for Render:**
```bash
gunicorn wsgi:app
```

**Build Command for Render:**
```bash
pip install -r requirements.txt && python data_generator.py
```

---

## 🔗 Post-Deployment

### Your App URLs

**Render**: `https://stock-screener-xxxx.onrender.com`  
**Heroku**: `https://stock-screener-app.herokuapp.com`  
**PythonAnywhere**: `https://yourusername.pythonanywhere.com`  
**Railway**: `https://stock-screener-production.up.railway.app`

### Test Your Deployment

1. Visit the URL
2. Search for a company
3. Create a screen
4. Export CSV
5. Toggle theme

---

## 🐛 Common Issues

### Issue 1: Build Fails

**Solution**: Check `requirements.txt` has all dependencies

### Issue 2: Database Not Found

**Solution**: Ensure build command includes `python data_generator.py`

### Issue 3: App Crashes

**Solution**: Check logs:
```bash
# Render: View logs in dashboard
# Heroku: heroku logs --tail
```

### Issue 4: Port Issues

**Solution**: Use environment variable:
```python
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
```

---

## 📊 Performance Tips

1. **Enable Caching**: Add Flask-Caching
2. **Compress Responses**: Add Flask-Compress
3. **Use CDN**: For static files
4. **Database Indexing**: Add indexes to frequently queried columns

---

## 🎉 Success!

Your Stock Screener is now live and accessible worldwide!

**Share your app**:
- Add to portfolio
- Share on LinkedIn
- Include in resume
- Demo to recruiters

---

**Deployment Status**: Ready ✅  
**Recommended Platform**: Render  
**Estimated Deploy Time**: 5 minutes