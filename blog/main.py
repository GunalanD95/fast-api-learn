from os import stat
from fastapi import FastAPI , status , Response , HTTPException
from fastapi import FastAPI, Depends
from pydantic.networks import HttpUrl
from . import schemas , models
from .db import engine ,SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext

models.Base.metadata.create_all(engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close




@app.post('/student' , status_code=status.HTTP_201_CREATED) # importing status and using it is a status code for our responses
def create(request: schemas.Student , db : Session = Depends(get_db)): # get db is used to make connection with our database
    new_student = models.Student(name=request.name,body =request.body)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


# get all the students which we created using post method 
@app.get('/student')
def all_students(db : Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students

# get all the students with ids
@app.get('/student/{id}' , status_code=200 ,response_model = schemas.ShowStudent ) #using the extended model class from schemas
def show(id:int,response: Response, db : Session = Depends(get_db)):
    # writing a query to get student record with {id} given and first is used to get the value that matches first
    student_id = db.query(models.Student).filter(models.Student.id == id).first()
    if not student_id:
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"data" : {f"student with id {id} is not found"}}
        raise HTTPException(status_code=400,detail=f"student with id {id} is not found")
    return student_id


# delete all the student with id
@app.delete('/student/{id}' , status_code=204)
def delete(id:int,response: Response, db : Session = Depends(get_db)):
    db.query(models.Student).filter(models.Student.id == id).delete(synchronize_session=False)
    db.commit()
    return "done"


# update all the student record with id
@app.put('/student/{id}' , status_code=status.HTTP_202_ACCEPTED)
def update(id:int,request: schemas.Student , db : Session = Depends(get_db)):
    stud = db.query(models.Student).filter(models.Student.id == id) # getting the record with the id from schema
    # db.query(models.Student).filter(models.Student.id == id).update(request) # update the record with update method
    if not stud.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f'student is not found with {id}')
    stud.update({'name':request.name,'body':request.body})  # update the record with update method
    db.commit()
    return "Success"


pass_context = CryptContext(schemes=["bcrypt"],deprecated="auto")


# Creating a user
@app.post('/user')
def create_user(request: schemas.User,db : Session = Depends(get_db)):
    hased_Password = pass_context.hash(request.passwd) #hasinng the password using passlib lib
    new_user = models.User(user_name=request.user_name,email =request.email,passwd =hased_Password)
    # new_user = models.User(request)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Getting the user
@app.get('/user/{id}')
def get_user(id:int,response: Response, db : Session = Depends(get_db)):
    user_id = db.query(models.User).filter(models.User.id == id).first()
    if not user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'the user with {id} is not found in the db') # for get method we dont need to commmit to db
    return user_id
