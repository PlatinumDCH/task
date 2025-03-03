from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "PhotoShare"
    PROJECT_VERSION: str = "1"
    PG_URL: str = "postgresql+asyncpg://test:000000@localhost:0000/test"
    SECRET_KEY_JWT: str = "secretkey"
    ALGORITHM: str = 'HS384'

    model_config = SettingsConfigDict(
        extra="ignore", env_file=".env", env_file_encoding="utf-8"
    )


settins = Settings()