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

###### CREATING USER API

Since we are going to have multiple apis , its better to have them as routers . for that we need to create router files and repo (to write function for apis) and finally we will include them in main.py

Create two folders inside app called repos and routers
create a user.py in both folders

In app/routers/user.py
```
from fastapi import APIRouter, Depends , Response  # importing api router
from .. import schemas , models , app
from ..app import engine ,SessionLocal
from sqlalchemy.orm import Session
from ..repos import user


router = APIRouter(
    tags=['users'],
    prefix="/user", # initializing /user as root page 
)

get_db = app.get_db # importing the db connection


# Creating a user
@router.post('/',response_model=schemas.User) # we are using response model to limit the respone body which we want to show using schema class
def create_user(request: schemas.User,db : Session = Depends(get_db)): # using schemas as request
    return user.create_user(request,db) # calling the create user fun from repo/user.py file

```

Now since repo/user.py we need to write fun to create user 

```
from fastapi import Depends , Response 
from .. import schemas , models , app
from ..app import engine ,SessionLocal
from sqlalchemy.orm import Session


# Creating a user
def create_user(request: schemas.User,db : Session):
    new_user = models.User(user_name=request.user_name,email =request.email,passwd =request.passwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

```


