import contextlib
from  typing import AsyncGenerator, Optional
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession


from src.core.config import settings

class DatabaseSessionManager:
    def __init__(self, url: str):
        self._url = url
        self._engine: Optional[AsyncEngine] = None
        self._session_maker: Optional[async_sessionmaker] = None

    async def _initialize(self):
        if self._engine is None or self._session_maker is None:
            self._engine = create_async_engine(self._url)
            self._session_maker = async_sessionmaker(
                autoflush=False, autocommit=False, bind=self._engine
            )
    
    async def close(self):
        if self._engine:
            await self._engine.dispose()
            self._engine = None
            self._session_maker = None

    @contextlib.asynccontextmanager
    async def session(self) -> AsyncGenerator[AsyncSession, None]:
        if self._session_maker is None:
            await self._initialize()

        if self._session_maker is None:
            raise Exception(
                "Session maker is not initialized"
            )

        session = self._session_maker()

        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
    
    @contextlib.asynccontextmanager
    async def lifespan(self):
        await self._initialize()
        try:
            yield
        finally:
            await self.close()

sessionmanager = DatabaseSessionManager(settings.PG_URL)

async def get_conn_db() -> AsyncGenerator[AsyncSession, None]:
    async with sessionmanager.lifespan():
        async with sessionmanager.session() as session:
            yield session