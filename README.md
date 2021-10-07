# fast-api-learn

##              FAST-API PROJECT DOCUMENTATION


###### Why FastAPI?
   FastAPI framework, high performance, easy to learn, fast to code, ready for production , it is one of the fastest modern python framework mainly used to build apis , it has currently ** 36.6k stars in github ** , also its support async and type hints which can give you better support.
   
######  INSTALL FASTAPI ?

```
pip3 install fastapi[all]
```

Also install uvicorn to work as the server:
```
pip3 install uvicorn[standard]
```

######  HOW TO CREATE API ?
create a folder called app , inside that create a main.py file and add these following lines there

from fastapi import FastAPI 

app = FastAPI() # initialization of the fastapi instance

```
@app.get("/") # routing the index page of the server
def index():
    return "HELLO WORLD"
```

then run your app using the following command:
```
uvicorn main:app --reload
```

Yup , thats it.



