import os

from sqlalchemy import (
    create_engine,
    Integer,
    Column,
    String,
    ForeignKey)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
conn = 'sqlite:///' + os.path.join(BASE_DIR, 'blog.db')

e = create_engine(conn, echo=True)

Base = declarative_base()

"""
class User(Base):
        id: int
        username: str
        email: str

class Post:
        id: int
        title: str
        content: str
        user_id: int foreignkey
"""


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(40), nullable=False)
    email = Column(String(40), nullable=False)
    posts = relationship('Posts', backref='author')

    def __repr__(self):
        return f'<User {self.username}>'


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer(), primary_key=True)
    title = Column(String(45), nullable=False)
    content = Column(String(255), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __repr__(self):
        return f'<User{self.title}>'


Base.metadata.create_all(e)
session = sessionmaker()(bind=e)
