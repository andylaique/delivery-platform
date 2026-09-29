"""Database engine and session management (PostgreSQL primary)."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from app.core.config import get_settings

settings = get_settings()

# SQLite needs a special flag; Postgres uses a small connection pool.
connect_args = {}
engine_kwargs = {
    "pool_pre_ping": True,
}

if settings.is_sqlite:
    connect_args = {"check_same_thread": False}
else:
    # Safe defaults for free-tier Postgres (Neon, Supabase, Render)
    engine_kwargs.update(
        {
            "pool_size": 5,
            "max_overflow": 10,
            "pool_recycle": 300,
        }
    )

engine = create_engine(
    settings.database_url,
    connect_args=connect_args,
    **engine_kwargs,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    """Yield a database session for one request, then close it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
