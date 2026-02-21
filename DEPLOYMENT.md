# Deployment Guide

## 🚀 Free Deployment Options

### Option 1: Render (Recommended)

1. **Push to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin your-repo-url
   git push -u origin main
   ```

2. **Deploy on Render**:
   - Go to https://render.com
   - Click "New" → "Web Service"
   - Connect your GitHub repo
   - Configure:
     - **Name**: codebase-qa-backend
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
     - **Root Directory**: `backend`

3. **Add Environment Variables**:
   - `GEMINI_API_KEY`: Your Gemini API key
   - `DATABASE_URL`: `sqlite:///./codebase_qa.db`

4. **Deploy**: Click "Create Web Service"

✅ **Free Tier**: 750 hours/month

---

### Option 2: Railway

1. **Install Railway CLI**:
   ```bash
   npm i -g @railway/cli
   ```

2. **Login & Deploy**:
   ```bash
   cd backend
   railway login
   railway init
   railway up
   ```

3. **Add Environment Variables**:
   - Go to Railway dashboard
   - Add `GEMINI_API_KEY`
   - Add `DATABASE_URL`

4. **Custom Domain** (optional):
   - Go to Settings → Networking
   - Add custom domain

✅ **Free Tier**: $5 credit/month

---

### Option 3: Fly.io

1. **Install Flyctl**:
   ```powershell
   powershell -Command "iwr https://fly.io/install.ps1 -useb | iex"
   ```

2. **Login**:
   ```bash
   fly auth login
   ```

3. **Launch App**:
   ```bash
   cd backend
   fly launch
   ```

4. **Set Secrets**:
   ```bash
   fly secrets set GEMINI_API_KEY=your_api_key_here
   ```

5. **Deploy**:
   ```bash
   fly deploy
   ```

✅ **Free Tier**: 3 shared-cpu-1x 256MB VMs

---

### Option 4: Vercel (Serverless)

**Note**: Vercel is better for Next.js. For Python FastAPI, use Render or Railway.

---

## 📝 Pre-Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] `requirements.txt` updated
- [ ] `.env` not in git (add to `.gitignore`)
- [ ] `Procfile` created
- [ ] `Dockerfile` created (for Railway/Fly.io)
- [ ] Environment variables documented
- [ ] Database setup (SQLite or upgrade to PostgreSQL)

---

## 🔒 Security Notes

1. **Never commit `.env` file**
2. **Use environment variables** for sensitive data
3. **Enable CORS** if frontend is on different domain
4. **Add rate limiting** for production

---

## 🌐 After Deployment

Your API will be available at:
- Render: `https://your-app-name.onrender.com`
- Railway: `https://your-app-name.railway.app`
- Fly.io: `https://your-app-name.fly.dev`

**Test endpoints**:
- GET `/` - Web UI
- GET `/docs` - API documentation
- GET `/status` - Health check
- POST `/upload/upload` - File upload
- POST `/qa/ask` - Ask questions

---

## 🔄 Updates

To update deployed app:

**Render**: Auto-deploys on git push

**Railway**: 
```bash
railway up
```

**Fly.io**:
```bash
fly deploy
```

---

## 💾 Database Upgrade (Optional)

For production, upgrade from SQLite to PostgreSQL:

1. **Add to requirements.txt**:
   ```
   psycopg2-binary==2.9.9
   ```

2. **Update DATABASE_URL**:
   ```
   DATABASE_URL=postgresql://user:password@host:5432/dbname
   ```

3. **Platform-specific**:
   - Render: Add PostgreSQL from dashboard
   - Railway: Add PostgreSQL plugin
   - Fly.io: `fly postgres create`

---

**Recommended**: Start with **Render** (easiest free deployment)
