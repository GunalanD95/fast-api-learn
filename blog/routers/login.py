from datetime import timedelta
from fastapi import APIRouter, Depends # importing api router
from fastapi import FastAPI , status , Response , HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from blog.token import ACCESS_TOKEN_EXPIRE_MINUTES

from .. import schemas , models , db
from ..db import engine ,SessionLocal
from sqlalchemy.orm import Session
from ..hash import Hash
from ..token import create_access_token

router = APIRouter(
    tags=['login']
)


get_db = db.get_db # importing the db connection

@router.post('/login')
def user_login(request:OAuth2PasswordRequestForm = Depends(),db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"the {request.username} id is not found in this db")
    if not Hash.verify(request.password,user.passwd): #verifying our password with hash 
        raise HTTPException(status_code=status.WS_1007_INVALID_FRAME_PAYLOAD_DATA,detail=f"Your password is incorrect")


    # if login success we need to generate a jwt token


    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data = {"sub": user.email}, expires_delta = access_token_expires
    )
    return {"access_token": access_token,"token_type":"bearer"}