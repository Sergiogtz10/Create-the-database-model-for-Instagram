import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'USER'

    id = Column(Integer, primary_key=True)
    User_name = Column(String(250), nullable=False)
    First_name = Column(String(250), nullable=False)
    Last_name = Column(String(250), nullable=False)
    Email = Column(String(250), nullable=False)

class Post(Base):
    __tablename__ = 'POST'
    
    id = Column(Integer, primary_key=True)
    Title = Column(String(250), nullable=False)
    Image = Column(String(250), nullable=False)
    User_id = Column(Integer, ForeignKey('USER.id'))
    user = relationship(User)
    
class Comment(Base):
    __tablename__ = 'COMMENT'

    id = Column(Integer, primary_key=True)
    Comment_text = Column(String(250), nullable=False)
    User_id = Column(Integer, ForeignKey('USER.id'))
    Post_id = Column(Integer, ForeignKey('POST.id'))
    user = relationship(User)
    post = relationship(Post)

class Media(Base):
    __tablename__ = 'MEDIA'

    id = Column(Integer, primary_key=True)
    Type = Column(Integer, nullable=False)
    Url = Column(String(250), nullable=False)
    Post_id = Column(Integer, ForeignKey('POST.id'))
    post = relationship(Post)

class Follower(Base):
    __tablename__ = 'FOLLOWER'
    id = Column(Integer, primary_key=True)
    User_from_id = Column(Integer, ForeignKey('USER.id'))
    User_to_id = Column(Integer, ForeignKey('USER.id'))
    user = relationship(User)
    

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')