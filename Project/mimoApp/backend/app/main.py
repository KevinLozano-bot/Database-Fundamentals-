from fastapi import FastAPI
from api import courses
from api import users
from api import auth
from api import Lesson
from api import enrollment



app = FastAPI(title="mimoApp API" , version="0.0.0")


app.include_router((auth.router), prefix="/auth", tags=["Auth"])
app.include_router((users.router), prefix="/users", tags=["Users"])
app.include_router((courses.router), prefix="/courses", tags=["Courses"])
app.include_router((Lesson.router), prefix="/lesson", tags=["Lesson"])
app.include_router((enrollment.router), prefix="/enrollment", tags=["Enrollment"])

@app.get("/")
def root(): 
    return {"message": "Welcome to MimoApp"}

