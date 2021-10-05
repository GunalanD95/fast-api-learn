from fastapi import APIRouter, Depends # importing api router
from fastapi import FastAPI , status , Response , HTTPException
from .. import schemas , models , db
from ..db import engine ,SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .. import hash
from ..repos import user
from .. import hash , oauth2
from ..repos import student

router = APIRouter(
    tags=['users'],
    prefix="/user", # initializing /user as root page 
)

get_db = db.get_db # importing the db connection


pass_context = CryptContext(schemes=["bcrypt"],deprecated="auto")


# Creating a user
@router.post('/',response_model=schemas.ShowUser) # we are using response model to limit the respone body which we want to show using schema class
def create_user(request: schemas.User,db : Session = Depends(get_db),get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.create_user(request,db)

# Getting the user
@router.get('/{id}')
def get_user(id:int,response: Response, db : Session = Depends(get_db),get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.get_user(id,response,db)