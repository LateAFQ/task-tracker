from typing import Any, AsyncIterable

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

# Type alias for the session factory
SessionFactoryType = async_sessionmaker[AsyncSession]


def create_sa_engine(url: str, **kwargs: Any) -> AsyncEngine:
    return create_async_engine(url, **kwargs)


def create_sa_session_factory(engine: AsyncEngine) -> SessionFactoryType:
    return async_sessionmaker(engine, autoflush=False, expire_on_commit=False)


async def create_sa_session(
    session_factory: SessionFactoryType,
) -> AsyncIterable[AsyncSession]:

    async with session_factory() as session:
        yield session
