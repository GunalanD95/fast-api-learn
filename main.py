from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/") # OPERATION(PATH OR ROUTE)
def index():
    return {'data':{"name":"Gunalan"}}


@app.get("/about")
def about():
    return{'data':{"name":"this is about page"}}


@app.get("/blog")  # LIMITING DATA TO 10  PUBLISHED BLOGS
def blog(limit=10,pub: bool= True ,sort : Optional[str] = None): # giving default values and sort as optional 

    #/blog?limit=50&pub=false

    if pub:
        return{"data":{f"total {limit} blog lists "}}
    else:
        return{"data":{"all blog lists "}}

@app.get("/blog/unpublished")
def unpublished():
    return{"data":{"all unpublished"}}

@app.get("/blog/{id}")
def show_blog(id: int): # id as type integer here 
    return{"data":id}


@app.get("/blog/{id}/comments")
def show_blog_comments(id: str):
    return{"data":"comments in blog"}


# creating blog using post method
@app.post("/blog")
def create():
    return {"data":{"blog":"the blog is created here"}}
