"""
Main menu module for MimoApp

This module contains the necessary functions to display an interactive menu and manage user selections for a Game Console.
and manage user selections for a Game Console.

AUTHORS: Kevin Estiven Lozano Duarte <kelozanod@udistrital.edu.co>

This file is part of PROJECT.

PROJECT is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version.

PROJECT is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with PROJECT. If not, see <https://www.gnu.org/licenses/>.

"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.auth import router as auth_router
from api.users import router as users_router
from api.courses import router as courses_router
from api.Lesson import router as lesson_router


app = FastAPI(
    title="mimoApp API",
    description="API para gestionar usuarios, cursos y lecciones en mimoApp.",
    version="1.0.0"
)


origins = [
    "http://localhost:3000",  
    "https://mimoapp.com"     
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(users_router, prefix="/users", tags=["Users"])
app.include_router(courses_router, prefix="/courses", tags=["Courses"])
app.include_router(lesson_router, prefix="/lesson", tags=["Lesson"])  


@app.get("/", tags=["Root"])
def root():
    """
    Welcome endpoint of the API.

    This is the root route of the API service, serving as an entry point to verify
    that the server is running correctly. 

    Returns:
        dict: A welcome message indicating that the API is functioning correctly.
    
    Example:
        {"message": "Welcome to MimoApp"}
    """
    return {"message": "Welcome to MimoApp"}
