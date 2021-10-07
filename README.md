# fast-api-learn

##              FAST-API PROJECT DOCUMENTATION


###### Why FastAPI?
   FastAPI framework, high performance, easy to learn, fast to code, ready for production , it is one of the fastest modern python framework mainly used to build apis , it has currently ** 36.6k stars in github **
   
######  HOW TO CREATE API ?

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return "YOU WILL BE SUCCESSFUL GUNA DONT WORRY JUST KEEP TRYING"


