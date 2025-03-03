from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "PhotoShare"
    PROJECT_VERSION: str = "1"
    PG_DRIVER: str = 'postgresql+asyncpg'
    PG_USER: str = "test"
    PG_PASSWORD: str = "test"
    PG_DATABASE: str = "db"
    PG_HOST: str = "test"
    PG_PORT: int = 5432
    PG_URL: str = 'postgresql+asyncpg://name:namepass@db:5432/name_database'
    SECRET_KEY_JWT: str = "secretkey"
    ALGORITHM: str = 'HS384'

    
    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=".env",
        env_file_encoding="utf-8"
    )


settings = Settings()