from fastapi import Depends # importing api router
from .. import schemas , models , db
from fastapi import FastAPI , status , Response , HTTPException
from ..db import engine ,SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .. import hash


pass_context = CryptContext(schemes=["bcrypt"],deprecated="auto")


# Creating a user
def create_user(request: schemas.User,db : Session):
    new_user = models.User(user_name=request.user_name,email =request.email,passwd =hash.Hash.encrypt_bcrypt(request.passwd)) # calling the encrypt_bcrypt from hash.py
    # new_user = models.User(request)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Getting the user
def get_user(id:int,response: Response, db : Session):
    user_id = db.query(models.User).filter(models.User.id == id).first()
    if not user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'the user with {id} is not found in the db') # for get method we dont need to commmit to db
    return user_id