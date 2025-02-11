from fastapi import FastAPI
from api import courses
from api import users
from api import auth



app = FastAPI(title="mimoApp API" , version="0.0.0")


app.include_router((auth.router), prefix="/auth", tags=["Auth"])
app.include_router((users.router), prefix="/users", tags=["Users"])
app.include_router((courses.router), prefix="/courses", tags=["Courses"])

@app.get("/")
def root(): 
    return {"message": "Welcome to MimoApp"}

