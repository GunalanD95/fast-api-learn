from pydantic import BaseModel


class Student(BaseModel):
    title : str
    body : set