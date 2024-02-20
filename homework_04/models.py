from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from config import DB_ASYNC_URL

# PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/psqldb"
engine = create_async_engine(DB_ASYNC_URL, echo=True)
session = async_sessionmaker(bind=engine, autocommit=False)
Base = declarative_base()
# def get_session():
#     with async_sessionmaker as se

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
