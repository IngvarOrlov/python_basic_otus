from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from config import DB_ASYNC_URL
# PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/psqldb"
engine = create_async_engine(DB_ASYNC_URL, echo=True)


def Session():
    session = AsyncSession(engine)
    return session
# session = AsyncSession(engine)

class Base(DeclarativeBase):
    pass


class IdMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)


class User(Base, IdMixin):
    __tablename__ = 'users'
    name = Column(String, nullable=False)
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    posts = relationship("Post", back_populates="user", uselist=True)


class Post(Base, IdMixin):
    __tablename__ = 'posts'
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, )
    title = Column(String, nullable=False)
    body = Column(String, default="")
    user = relationship("User", back_populates="posts", uselist=False)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

