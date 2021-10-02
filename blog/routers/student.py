from fastapi import APIRouter, Depends # importing api router
from fastapi import FastAPI , status , Response , HTTPException
from .. import schemas , models , db
from ..db import engine ,SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .. import hash


get_db = db.get_db # importing the db connection


router = APIRouter(
    tags=['students']
)

@router.get('/student')
def all_students(db : Session = Depends(db.get_db)):
    students = db.query(models.Student).all()
    return students



@router.post('/student' , status_code=status.HTTP_201_CREATED) # importing status and using it is a status code for our responses
def create(request: schemas.Student , db : Session = Depends(get_db)): # get db is used to make connection with our database
    new_student = models.Student(name=request.name,body =request.body,user_id=request.user_name) #user_id is linked to users table
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student



# get all the students with ids
@router.get('/student/{id}' , status_code=200 ,response_model = schemas.ShowStudent) #using the extended model class from schemas
def show(id:int,response: Response, db : Session = Depends(get_db)):
    # writing a query to get student record with {id} given and first is used to get the value that matches first
    student_id = db.query(models.Student).filter(models.Student.id == id).first()
    if not student_id:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"data" : {f"student with id {id} is not found"}}
        raise HTTPException(status_code=400,detail=f"student with id {id} is not found")
    return student_id


# delete all the student with id
@router.delete('/student/{id}' , status_code=204)
def delete(id:int,response: Response, db : Session = Depends(get_db)):
    db.query(models.Student).filter(models.Student.id == id).delete(synchronize_session=False)
    db.commit()
    return "done"


# update all the student record with id
@router.put('/student/{id}' , status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request: schemas.Student , db : Session = Depends(get_db)):
    stud = db.query(models.Student).filter(models.Student.id == id) # getting the record with the id from schema
    # db.query(models.Student).filter(models.Student.id == id).update(request) # update the record with update method
    if not stud.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'student is not found with {id}')
    stud.update({'name':request.name,'body':request.body})  # update the record with update method
    db.commit()
    return "Success"
    