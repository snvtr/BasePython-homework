"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, joinedload
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    ForeignKey
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql://postgres:12345@localhost/postgres" #+asyncpg

engine = create_engine(PG_CONN_URI, echo=True)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
Base    = declarative_base(bind=engine)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    name = Column(String(100), unique=True, nullable=False)
    email = Column(String(500), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow) # , server_default=func.now()

    posts = relationship("Post", back_populates="user")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username!r}, is_staff={self.email}, created_at={self.created_at!r})"

    def __repr__(self):
        return str(self)

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), unique=True, nullable=False)
    body = Column(String(1000), nullable=False)
#    created_at = Column(DateTime, nullable=False, default=datetime.utcnow) # , server_default=func.now()
    user_id = Column(Integer, ForeignKey(User.id))
#    parent_id  = Column(Integer, default=-1)

    user = relationship(User, back_populates="posts")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title!r}, body={self.body}, created_at={self.created_at!r}, created_by={self.created_by!r}, parent_id={self.parent_id!r})"

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    Base.metadata.create_all()
