# creating and connecting the db with our FastApi App
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#engine = create_engine('sqlite:///./blog.db',echo=True)
#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})


Base = declarative_base()

SessionLocal = sessionmaker(bind= engine , autocommit=False, autoflush=False)