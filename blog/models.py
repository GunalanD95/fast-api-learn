import re

from sqlalchemy.sql.schema import ForeignKey
from blog.db import Base
from sqlalchemy import Column, Integer , String , ForeignKey
from sqlalchemy.orm import relationship

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    body = Column(String)
    user_id = Column(String, ForeignKey('users.user_name'))
    user_details = relationship("User", back_populates="student") # make a relationship with two tables using sql alchemy orm method


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    user_name = Column(String)
    email = Column(String)
    passwd = Column(String)
    student = relationship("Student", back_populates="user_details")