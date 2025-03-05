from fastapi.testclient import TestClient
import pytest
import pytest_asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from httpx import AsyncClient
from src.database import get_conn_db
from src.models import Base
from src.main import app


DATABASE_URL = "sqlite+aiosqlite:///:memory:"
engine = create_async_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


TestingSessionLocal = async_sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession,
)


@pytest_asyncio.fixture()
async def test_database():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    
    async with TestingSessionLocal() as session:
        yield session

    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
    await engine.dispose()


@pytest_asyncio.fixture()
async def testdatabase(test_database):
    async def override_get_db():
        yield test_database
    
    app.dependency_overrides[get_conn_db] = override_get_db

@pytest_asyncio.fixture()
async def fastapi_testclient():
    client = TestClient(app)
    return client
