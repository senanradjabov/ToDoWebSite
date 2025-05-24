from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.pool import AsyncAdaptedQueuePool, NullPool

from app.core.config import ModeEnum, settings

engine = create_async_engine(
    str(settings.ASYNC_POSTGRES_URL),
    echo=False,
    poolclass=NullPool
    if ModeEnum.testing == settings.MODE
    else AsyncAdaptedQueuePool,  # Asyncio pytest works with NullPool
)
SessionLocal = async_sessionmaker(
    bind=engine, class_=AsyncSession, expire_on_commit=False
)
