from blog.db import Base
from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    name : str
    body : str
    user_name: str

# # Extending the Student model and using in the show/get method
# class ShowStudent(Student):
#     class Config:
#         orm_mode = True    # need to add this line since we are using sql alchemy db we need this to interact orm model with the api



# Extending the BaseModel model and using in the show/get method and displaying only the records which we want to show
class ShowStudent(BaseModel):
    name : str # will show only the name
    class Config():
        orm_mode = True    # need to add this line since we are using sql alchemy db we need this to interact with the api



# Creating a Schema for User

class User(BaseModel):
    user_name:str
    email:str
    passwd:str

class ShowUser(BaseModel):
    user_name:str
    email:str

    class Config():
        orm_mode = True  


class Login(BaseModel):
    email:str
    passwd:str

    class Config():
        orm_mode = True  


class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None