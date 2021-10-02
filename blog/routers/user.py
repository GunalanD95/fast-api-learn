from fastapi import APIRouter, Depends # importing api router
from fastapi import FastAPI , status , Response , HTTPException
from .. import schemas , models , db
from ..db import engine ,SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .. import hash

router = APIRouter(
    tags=['users'],
    prefix="/user", # initializing /user as root page 
)

get_db = db.get_db # importing the db connection


pass_context = CryptContext(schemes=["bcrypt"],deprecated="auto")


# Creating a user
@router.post('/',response_model=schemas.ShowUser) # we are using response model to limit the respone body which we want to show using schema class
def create_user(request: schemas.User,db : Session = Depends(get_db)):
    new_user = models.User(user_name=request.user_name,email =request.email,passwd =hash.Hash.encrypt_bcrypt(request.passwd)) # calling the encrypt_bcrypt from hash.py
    # new_user = models.User(request)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Getting the user
@router.get('/{id}')
def get_user(id:int,response: Response, db : Session = Depends(get_db)):
    user_id = db.query(models.User).filter(models.User.id == id).first()
    if not user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'the user with {id} is not found in the db') # for get method we dont need to commmit to db
    return user_id