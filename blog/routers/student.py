from fastapi import APIRouter, Depends # importing api router
from .. import schemas , models , db
from ..db import engine ,SessionLocal
from sqlalchemy.orm import Session

router = APIRouter()

@router.get('/student', tags=['student'])
def all_students(db : Session = Depends(db.get_db)):
    students = db.query(models.Student).all()
    return students