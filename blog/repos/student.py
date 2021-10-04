from fastapi import Depends # importing api router
from .. import schemas , models , db
from fastapi import FastAPI , status , Response , HTTPException
from ..db import engine ,SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from .. import hash , oauth2



# Writing functions for our routers

# function for '/student'
def get_all_students(db : Session,get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    students = db.query(models.Student).all()
    return students


# function to create a student
def create_student(request: schemas.Student , db : Session): # get db is used to make connection with our database
    new_student = models.Student(name=request.name,body =request.body,user_id=request.user_name) #user_id is linked to users table
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


# get all the students with ids
def show_student(id:int,response: Response, db : Session,get_current_user: schemas.User = Depends(oauth2.get_current_user)):
    # writing a query to get student record with {id} given and first is used to get the value that matches first
    student_id = db.query(models.Student).filter(models.Student.id == id).first()
    if not student_id:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"data" : {f"student with id {id} is not found"}}
        raise HTTPException(status_code=400,detail=f"student with id {id} is not found")
    return student_id


# delete all the student with id
def delete_student(id:int,response: Response, db : Session):
    db.query(models.Student).filter(models.Student.id == id).delete(synchronize_session=False)
    db.commit()
    return "done"

# delete all the student with id
def update_student(id:int,request: schemas.Student , db : Session):
    stud = db.query(models.Student).filter(models.Student.id == id) # getting the record with the id from schema
    # db.query(models.Student).filter(models.Student.id == id).update(request) # update the record with update method
    if not stud.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'student is not found with {id}')
    stud.update({'name':request.name,'body':request.body})  # update the record with update method
    db.commit()
    return "Success"