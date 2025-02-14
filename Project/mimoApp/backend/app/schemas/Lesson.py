from pydantic import BaseModel
from typing import Optional

class LessonCreate(BaseModel):
    """
    Schema for creating a new lesson.

    This schema is used to validate the request body when creating a new lesson.
    It includes the title and description of the lesson.

    Attributes:
        title (str): The title of the lesson. It must be unique.
        description (str): The detailed description of the lesson.
    """
    title: str
    description: str


class LessonResponse(BaseModel):
    """
    Schema for the lesson response.

    This schema is used to return the information of a lesson in the API response.
    It includes the lesson ID, title, and description.

    Attributes:
        id (int): The unique identifier of the lesson.
        title (str): The title of the lesson.
        description (str): The description of the lesson.
    """
    id: int
    title: str
    description: str

    class Config:
        """
        Configuration for the Pydantic model.

        Enables ORM mode to allow the model to be used with SQLAlchemy objects.
        """
        orm_mode = True  # Required to work with SQLAlchemy ORM


class LessonUpdate(BaseModel):
    """
    Schema for updating an existing lesson.

    This schema is used to validate the request body when updating a lesson.
    All fields are optional, allowing partial updates of attributes.

    Attributes:
        title (Optional[str]): The updated title of the lesson.
        description (Optional[str]): The updated description of the lesson.
    """
    title: Optional[str] = None  # Fields are optional for partial updates
    description: Optional[str] = None
