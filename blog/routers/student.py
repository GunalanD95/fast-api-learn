from fastapi import APIRouter, Depends # importing api router
from fastapi import FastAPI , status , Response , HTTPException
from .. import schemas , models , db
from ..db import engine ,SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .. import hash
from ..repos import student


get_db = db.get_db # importing the db connection


router = APIRouter(
    tags=['students']
)

@router.get('/student')
def all_students(db : Session = Depends(db.get_db)):
    return student.get_all_students(db) # calling our get method fun from repos directory 



@router.post('/student' , status_code=status.HTTP_201_CREATED) # importing status and using it is a status code for our responses
def create(request: schemas.Student , db : Session = Depends(get_db)): # get db is used to make connection with our database
    return student.create_student(request,db)



# get all the students with ids
@router.get('/student/{id}' , status_code=200 ,response_model = schemas.ShowStudent) #using the extended model class from schemas
def show(id:int,response: Response, db : Session = Depends(get_db)):
    return student.show_student(id,response,db)


# delete all the student with id
@router.delete('/student/{id}' , status_code=204)
def delete(id:int,response: Response, db : Session = Depends(get_db)):
    return student.delete_student(id,response,db)


# update all the student record with id
@router.put('/student/{id}' , status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request: schemas.Student , db : Session = Depends(get_db)):
    return student.update_student(id,request,db)
    