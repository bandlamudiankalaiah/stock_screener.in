# 🚀 Quick Deployment Guide

## ⚡ 5-Minute Render Deployment

### ✅ Files Already Created:
- `requirements.txt` (with gunicorn)
- `wsgi.py` (production entry point)
- `render.yaml` (Render config)
- `runtime.txt` (Python version)
- `.gitignore` (exclude unnecessary files)

---

## 📝 Step-by-Step

### 1️⃣ Push to GitHub (2 minutes)

```bash
# Initialize git
git init

# Add files
git add .

# Commit
git commit -m "Stock Screener - Ready for deployment"

# Create repo on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/stock-screener.git
git branch -M main
git push -u origin main
```

---

### 2️⃣ Deploy on Render (3 minutes)

1. Go to **https://render.com**
2. Click **"Sign Up"** (use GitHub)
3. Click **"New +"** → **"Web Service"**
4. Select your **stock-screener** repository
5. Fill in:
   ```
   Name: stock-screener
   Environment: Python 3
   Build Command: pip install -r requirements.txt && python data_generator.py
   Start Command: gunicorn wsgi:app
   Instance Type: Free
   ```
6. Click **"Create Web Service"**

---

### 3️⃣ Wait & Access

- Build takes **2-5 minutes**
- You'll get a URL: `https://stock-screener-xxxx.onrender.com`
- **Done!** 🎉

---

## 🎯 Alternative: Local Testing with Production Server

```bash
# Install gunicorn
pip install gunicorn

# Test production mode
gunicorn wsgi:app

# Access at: http://127.0.0.1:8000
```

---

## ❌ DON'T Use for Deployment:

```bash
# ❌ This is ONLY for local development
python app.py
```

---

## ✅ DO Use for Deployment:

### Render Start Command:
```bash
gunicorn wsgi:app
```

### Render Build Command:
```bash
pip install -r requirements.txt && python data_generator.py
```

---

## 🔧 If Deployment Fails

### Check These:

1. **requirements.txt** has gunicorn:
   ```
   Flask==3.0.0
   Flask-SQLAlchemy==3.1.1
   pandas==2.1.4
   gunicorn==21.2.0
   ```

2. **wsgi.py** exists and contains:
   ```python
   from app import app
   
   if __name__ == "__main__":
       app.run()
   ```

3. **Build command** includes database setup:
   ```bash
   pip install -r requirements.txt && python data_generator.py
   ```

---

## 📊 What Happens During Deployment

1. Render clones your GitHub repo
2. Installs Python 3.11
3. Runs: `pip install -r requirements.txt`
4. Runs: `python data_generator.py` (creates database)
5. Starts: `gunicorn wsgi:app` (production server)
6. Assigns a public URL
7. Your app is LIVE! 🚀

---

## 🎉 Success Checklist

After deployment:

- [ ] Visit your Render URL
- [ ] Search for "RELIANCE"
- [ ] View company details
- [ ] Create a custom screen
- [ ] Toggle dark theme
- [ ] Export CSV
- [ ] Share with friends! 🎊

---

## 📱 Share Your App

**Your Live URL**: `https://stock-screener-xxxx.onrender.com`

Share on:
- LinkedIn
- Portfolio website
- Resume
- GitHub README

---

## 🆘 Need Help?

**Render Logs**: Check deployment logs in Render dashboard

**Common Issues**:
- Build fails → Check requirements.txt
- App crashes → Check Render logs
- Database empty → Ensure build command runs data_generator.py

---

**Total Time**: 5 minutes  
**Cost**: FREE  
**Difficulty**: Easy ✅