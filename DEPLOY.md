# Deploy guide

## 1. Database (Neon)

1. Create a free project at [neon.tech](https://neon.tech)
2. Copy the connection string (use the **pooled** one if available)
3. Append `?sslmode=require` if not present

Example:
```
postgresql+psycopg2://user:pass@ep-xxx.region.aws.neon.tech/neondb?sslmode=require
```

## 2. Backend on Render

1. New → Web Service → connect this GitHub repo
2. **Root Directory:** `backend`
3. **Build Command:** `pip install -r requirements.txt`
4. **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`

Environment variables:

```
DATABASE_URL=postgresql+psycopg2://...neon...
SECRET_KEY=<long-random-string-64+>
DEBUG=false
ENVIRONMENT=production
CORS_ORIGINS=https://your-frontend.vercel.app
COOKIE_SECURE=true
UPLOAD_DIR=./uploads
```

Deploy. Check `https://your-api.onrender.com/health`

Seed manager (Render shell or locally against Neon):
```bash
python seed.py
```

Free Render services sleep after inactivity; first request may be slow.

## 3. Frontend on Vercel

1. Import this GitHub repo
2. **Root Directory:** `frontend`
3. Framework: Next.js
4. Env:
```
NEXT_PUBLIC_API_URL=https://your-api.onrender.com/api
```
5. Deploy. Update backend `CORS_ORIGINS` to the Vercel URL and redeploy API if needed.

## 4. Local Postgres (optional)

```bash
docker compose up -d
# backend/.env
DATABASE_URL=postgresql+psycopg2://postgres:postgres@localhost:5432/delivery
```

## Checklist before going public

- [ ] Strong SECRET_KEY (64+ random characters)
- [ ] DEBUG=false
- [ ] CORS_ORIGINS only your real frontend URL
- [ ] Postgres with SSL
- [ ] Manager password changed after first login
- [ ] Do not commit .env
