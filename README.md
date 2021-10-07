# fast-api-learn

##              FAST-API PROJECT DOCUMENTATION


###### Why FastAPI?
   FastAPI framework, high performance, easy to learn, fast to code, ready for production , it is one of the fastest modern python framework mainly used to build apis , it has currently ** 36.6k stars in github ** , also its support async and type hints which can give you better support.
   
######  INSTALL FASTAPI ?

```
pip3 install fastapi[all]
```

Also install uvicorn to work as the server:
```
pip3 install uvicorn[standard]
```

######  HOW TO CREATE API ?
create a folder called app , inside that create a main.py file and add these following lines there

from fastapi import FastAPI 

app = FastAPI() # initialization of the fastapi instance

```
@app.get("/") # routing the index page of the server
def index():
    return "HELLO WORLD"
```

then run your app using the following command:
```
uvicorn main:app --reload
```

Yup , thats it.

######  WHAT WE ARE GOING BUILD IN THIS PROJECT ?
 We will be creating a user table  with authentication to routes and student table with details 
 - CREATE STUDENT AND USER
 - DELETE STUDENT AND USER
 - UPDATE TABLES
 - GET METHOD TO FETCH DETAILS USING SPECIFIC IDS 
 - AUTHENTICATION USING JWT


Lets Build our user apis

######  We will create schemas for for user apis and use them  in response using pydantic

Inside app folder create a schemas.py file

```
from pydantic import BaseModel

# Creating a Schema for User
Class User(BaseModel):
   user_name:str
   email:str
   passwd:str
   
```

 ######  creating a engine and db connection using sqlalchemy 
 
 create a db file to store our tables , inside app folder create a app.db file
 ```
 # creating and connecting the db with our FastApi App
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False})


Base = declarative_base() #Now we will use in models which returns a orm classes.

SessionLocal = sessionmaker(bind= engine , autocommit=False, autoflush=False) # creating a session local for class instance

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close
```

######  creating user table using SQLAlchemy models

```
create a models file to create user table , inside app folder create a models.py file
from .app import Base # importing the base class from db file
from sqlalchemy import Column, Integer , String , ForeignKey # importing the data types

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,index=True)
    user_name = Column(String)
    email = Column(String)
    passwd = Column(String)
```

Now we have a db connection , schemas for our response models and models for tables , lets create our user APis



