from os import stat
from fastapi import FastAPI , status , Response , HTTPException
from fastapi import FastAPI, Depends
from pydantic.networks import HttpUrl
from . import schemas , models
from .db import engine ,SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from . import hash



models.Base.metadata.create_all(engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close




@app.post('/student' , status_code=status.HTTP_201_CREATED, tags=['student']) # importing status and using it is a status code for our responses
def create(request: schemas.Student , db : Session = Depends(get_db)): # get db is used to make connection with our database
    new_student = models.Student(name=request.name,body =request.body,user_id=request.user_name) #user_id is linked to users table
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


# get all the students which we created using post method 
@app.get('/student', tags=['student'])
def all_students(db : Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students

# get all the students with ids
@app.get('/student/{id}' , status_code=200 ,response_model = schemas.ShowStudent , tags=['student']) #using the extended model class from schemas
def show(id:int,response: Response, db : Session = Depends(get_db)):
    # writing a query to get student record with {id} given and first is used to get the value that matches first
    student_id = db.query(models.Student).filter(models.Student.id == id).first()
    if not student_id:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"data" : {f"student with id {id} is not found"}}
        raise HTTPException(status_code=400,detail=f"student with id {id} is not found")
    return student_id


# delete all the student with id
@app.delete('/student/{id}' , status_code=204, tags=['student'])
def delete(id:int,response: Response, db : Session = Depends(get_db)):
    db.query(models.Student).filter(models.Student.id == id).delete(synchronize_session=False)
    db.commit()
    return "done"


# update all the student record with id
@app.put('/student/{id}' , status_code=status.HTTP_202_ACCEPTED, tags=['student'])
def update(id:int,request: schemas.Student , db : Session = Depends(get_db)):
    stud = db.query(models.Student).filter(models.Student.id == id) # getting the record with the id from schema
    # db.query(models.Student).filter(models.Student.id == id).update(request) # update the record with update method
    if not stud.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'student is not found with {id}')
    stud.update({'name':request.name,'body':request.body})  # update the record with update method
    db.commit()
    return "Success"



###------------------------USER APIS---------------------###

pass_context = CryptContext(schemes=["bcrypt"],deprecated="auto")


# Creating a user
@app.post('/user',response_model=schemas.ShowUser, tags=['users']) # we are using response model to limit the respone body which we want to show using schema class
def create_user(request: schemas.User,db : Session = Depends(get_db)):
    new_user = models.User(user_name=request.user_name,email =request.email,passwd =hash.Hash.encrypt_bcrypt(request.passwd)) # calling the encrypt_bcrypt from hash.py
    # new_user = models.User(request)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Getting the user
@app.get('/user/{id}',tags=['users'])
def get_user(id:int,response: Response, db : Session = Depends(get_db)):
    user_id = db.query(models.User).filter(models.User.id == id).first()
    if not user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'the user with {id} is not found in the db') # for get method we dont need to commmit to db
    return user_id
