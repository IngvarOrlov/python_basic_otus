from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from config import DB_ASYNC_URL

# PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/psqldb"
engine = create_async_engine(DB_ASYNC_URL, echo=True)
session = AsyncSession(bind=engine, autocommit=False)
Base = declarative_base()


class IdMixin:
    Column("id", Integer, primary_key=True, autoincrement=True)


class User(Base, IdMixin):
    Column("name", String, nullable=False)
    Column("username", String, nullable=False, unique=True)
    Column("email", String, nullable=False, unique=True)
    posts = relationship("Post", back_populates="user", uselist=True)





class Post(Base, IdMixin):
    Column("user_id", Integer, nullable=False)
    Column("title", String, nullable=False)
    Column("body", String, default="")
    user = relationship("User", back_populates="posts", uselist=False)


"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user

- доработайте модуль `models`:
    - создайте асинхронный алхимичный `engine` (при помощи `create_async_engine`)
    - добавьте `declarative base`
    - создайте объект `Session` на основе класса `AsyncSession`
    - добавьте модели `User` и `Post`, объявите поля:
        - для модели `User` обязательными являются `name`, `username`, `email`
        - для модели `Post` обязательными являются `user_id`, `title`, `body`
        - создайте связи `relationship` между моделями: `User.posts` и `Post.user`
"""
