# creating and connecting the db with our FastApi App
from sqlalchemy import create_engine


#engine = create_engine('sqlite:///./blog.db',echo=True)
#SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

engine = create_engine('sqlite:///./blog.db',echo=True)