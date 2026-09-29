# Delivery Platform

Multi-role delivery system: **Manager**, **Vendor**, **Client**.

## Stack

| Layer | Technology |
|-------|------------|
| API | FastAPI + SQLAlchemy + PostgreSQL |
| Frontend | Next.js (pages router) |
| Auth | JWT in httpOnly cookies |
| Deploy | Render (API) + Vercel (frontend) + Neon (Postgres) |

See **DEPLOY.md** for production steps.

## Roles

- **Manager** – approve vendors, manage issues, platform overview
- **Vendor** – products, orders, clients, settings, delivery cost
- **Client** – browse vendors, place orders, track, rate, report issues

## Local development

### Backend

```bash
cd backend
cp .env.example .env   # set DATABASE_URL, SECRET_KEY
pip install -r requirements.txt
python seed.py         # creates manager account
uvicorn app.main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
cp .env.local.example .env.local
npm install
npm run dev
```

Open http://localhost:3000

Default manager (from seed): check seed.py / console output for credentials.
