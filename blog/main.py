from fastapi import FastAPI 
from . import  models
from .db import engine 
from . routers import student , user , login

models.Base.metadata.create_all(engine)

app = FastAPI()

app.include_router(student.router) # importing the student router which we created in routers file
app.include_router(user.router) 
app.include_router(login.router) 


