from fastapi import FastAPI
from . import schemas


app = FastAPI()

@app.post('/student')
def create(request: schemas.Student):
    return {
        "title":request.title,
        "body":request.body
    }