"""Application settings from environment variables."""

from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    app_name: str = "DeliveryPlatform"
    environment: str = "development"
    debug: bool = False

    secret_key: str = "change-me-in-production-use-a-long-random-string"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    refresh_token_expire_days: int = 7

    # PostgreSQL (preferred). Example:
    # postgresql+psycopg2://user:pass@host:5432/delivery
    # Local fallback uses SQLite only if DATABASE_URL is unset.
    database_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432/delivery"

    cors_origins: str = "http://localhost:3000"
    upload_dir: str = "./uploads"
    max_upload_size_mb: int = 5
    allowed_image_types: str = "image/jpeg,image/png,image/webp"

    rate_limit: str = "100/minute"
    cookie_secure: bool = False
    cookie_samesite: str = "lax"

    @property
    def cors_origins_list(self) -> List[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]

    @property
    def allowed_image_types_list(self) -> List[str]:
        return [t.strip() for t in self.allowed_image_types.split(",") if t.strip()]

    @property
    def is_sqlite(self) -> bool:
        return self.database_url.startswith("sqlite")


@lru_cache
def get_settings() -> Settings:
    return Settings()
