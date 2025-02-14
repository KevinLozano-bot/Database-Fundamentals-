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
from api import courses
from api import users
from api import auth
from api import lesson  

# Create the FastAPI instance
app = FastAPI(title="mimoApp API", version="0.0.0")

# Include the routers for different routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(courses.router, prefix="/courses", tags=["Courses"])
app.include_router(lesson.router, prefix="/lesson", tags=["Lesson"])  

# Root endpoint
@app.get("/")
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
