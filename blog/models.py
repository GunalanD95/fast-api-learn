from blog.db import Base
from sqlalchemy import Column, Integer , String


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String)
    body = Column(String)


class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    user_name = Column(String)
    email = Column(String)
    passwd = Column(String)