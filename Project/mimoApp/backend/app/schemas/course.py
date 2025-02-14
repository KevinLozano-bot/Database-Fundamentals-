from pydantic import BaseModel

class CourseCreate(BaseModel):
    """
    Schema for creating a new course.

    This schema is used to validate the request body when creating a new course.
    It includes the title and description of the course.

    Attributes:
        title (str): The title of the course.
        description (str): A detailed description of the course.
    """
    title: str
    description: str


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
    id: int
    title: str
    description: str

    class Config:
        """
        Configuration for Pydantic model.

        This configuration enables the ORM mode, allowing the model to be used 
        with SQLAlchemy objects.
        """
        orm_mode = True

        from_attributes = True