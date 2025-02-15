from pydantic import BaseModel, Field

class CourseCreate(BaseModel):
    """
    Schema for creating a new course.

    This schema is used to validate the request body when creating a new course.
    It includes the title and description of the course.

    Attributes:
        title (str): The title of the course.
        description (str): A detailed description of the course.
    """
    id: int = Field(..., description="The unique identifier of the course", example=1)
    title: str = Field(..., description="The title of the course", example="Introduction to FastAPI")
    description: str = Field(..., description="Detailed description of the course", example="Learn the basics of FastAPI and building APIs.")

class CourseUpdate(BaseModel):
    """
    Schema for updating an existing course.

    This schema is used to validate the request body when updating a course.
    All fields are optional, allowing partial updates of attributes.

    Attributes:
        title (str): The updated title of the course.
        description (str): The updated description of the course.
    """
    id: int = Field(..., description="The unique identifier of the course", example=1)
    title: str = Field(None, description="The updated title of the course", example="FastAPI Essentials")
    description: str = Field(None, description="The updated description of the course", example="Essential concepts and features of FastAPI.")

class CourseResponse(BaseModel):
    """
    Schema for the course response.

    This schema is used for returning course information in the API response.
    It includes the ID, title, and description of the course.

    Attributes:
        id (int): The unique identifier of the course.
        title (str): The title of the course.
        description (str): A detailed description of the course.
    """
    id: int = Field(..., description="The unique identifier of the course", example=1)
    title: str = Field(..., description="The title of the course", example="Introduction to FastAPI")
    description: str = Field(..., description="Detailed description of the course", example="Learn the basics of FastAPI and building APIs.")

    class Config:
        """
        Configuration for Pydantic model.

        This configuration enables the ORM mode, allowing the model to be used 
        with SQLAlchemy objects.
        """
        orm_mode = True
        from_attributes = True
