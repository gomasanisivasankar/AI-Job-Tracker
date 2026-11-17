from sqlalchemy.ext.asyncio import  create_async_engine,async_sessionmaker
from app.core.config import settings


# Create the SQLAlchemy engine using the database URL from settings
engine = create_async_engine(settings.database_url)

SessionLocal = async_sessionmaker(engine, expire_on_commit=False)

async def get_db():
    async with SessionLocal() as session:
        yield session