from fastapi import FastAPI
from fastapi import FastAPI, Depends
from . import schemas , models
from .db import engine ,SessionLocal
from sqlalchemy.orm import Session

models.Base.metadata.create_all(engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close




@app.post('/student' , status_code=201)
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
@app.get('/student/{id}')
def show(id:int, db : Session = Depends(get_db)):
    # writing a query to get student record with {id} given and first is used to get the value that matches first
    student_id = db.query(models.Student).filter(models.Student.id == id).first()
    return student_id