"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import asyncio
import os

from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    AsyncEngine,
    create_async_engine,
    async_scoped_session,
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, declared_attr

PG_CONN_URL = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://postgres:password@localhost/homework_04"
)


class Base:
    """
    Parent class for all database element.
    declarative_base(cls=Base) from sqlalchemy.orm is applied below to define this class as base.
    """

    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


Base = declarative_base(cls=Base)


class User(Base):
    """
    Class 'User':
    Post.user relationship specified. Parameter uselist=true shows the possibility of the existence
    of several posts by one author (user).
    """

    name = Column(String(50))
    username = Column(String(20), unique=True)
    email = Column(String(50), unique=True)

    posts = relationship("Post", back_populates="user", uselist=True)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}, username={self.username!r})"


class Post(Base):
    """
    Class 'Post':
    User.posts relationship spicified.
    """

    title = Column(String(200), unique=False, nullable=False)
    body = Column(Text, nullable=False, default="N/A")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    user = relationship("User", back_populates="posts")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, author_id={self.user_id})"


#  Engine and session creation
async_engine: AsyncEngine = create_async_engine(
    PG_CONN_URL,
    echo=False,
)
async_session = sessionmaker(async_engine, class_=AsyncSession, expire_on_commit=False)
Session = async_scoped_session(async_session, scopefunc=asyncio.current_task)
