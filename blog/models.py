from ast import Str
import email
from xmlrpc.client import Boolean
from pydantic import StrictBool
from sqlalchemy import BOOLEAN, Column,Integer,String,ForeignKey
from blog.database import Base
from sqlalchemy.orm import relationship
import datetime

from blog.schemas import Attendance

class Blog(Base):
    __tablename__='blogs'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)
    user_id=Column(Integer,ForeignKey('users.id'))

    creator=relationship("User",back_populates="blogs")

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    roll=Column(String)
 
    blogs=relationship('Blog',back_populates="creator")
    attendance=relationship('Atten',back_populates="creator2")

class Atten(Base):
    __tablename__='attendance'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    roll=Column(String)
    user_id=Column(Integer,ForeignKey('users.id'))
    date_time=Column(String)
    status_now=Column(BOOLEAN)

    creator2=relationship("User",back_populates="attendance")




