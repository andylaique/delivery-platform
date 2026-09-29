"""Seed manager account for development / first deploy."""

from app.core.database import SessionLocal, engine, Base
from app.core.security import hash_password
from app.models import User, Product, Order, OrderItem, Rating, Issue  # noqa: F401
from app.models.user import User, UserRole

Base.metadata.create_all(bind=engine)
db = SessionLocal()

try:
    existing = db.query(User).filter(User.phone == "+250780000000").first()
    if not existing:
        manager = User(
            phone="+250780000000",
            email="manager@delivery.local",
            hashed_password=hash_password("Manager123!"),
            full_name="Platform Manager",
            role=UserRole.MANAGER,
            is_active=True,
            is_verified=True,
            email_verified=True,
            contact_phone="+250780000000",
        )
        db.add(manager)
        db.commit()
        print("Created manager phone +250780000000 / Manager123!")
    else:
        print("Manager already exists")
finally:
    db.close()
