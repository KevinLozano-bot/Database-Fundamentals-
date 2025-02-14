from pydantic import BaseModel

class UserBase(BaseModel):
    """
    Base schema for user information.

    This schema serves as a base for other user-related schemas.
    It includes the common attributes shared by multiple user actions.

    Attributes:
        username (str): The unique username of the user.
        email (str): The email address of the user.
    """
    username: str
    email: str


class UserCreate(UserBase):
    """
    Schema for creating a new user.

    This schema is used to validate the request body when creating a new user.
    It extends the UserBase schema and includes the password attribute.

    Attributes:
        password (str): The password for the new user. Required during user registration.
    """
    password: str  # Only used when creating a new user


class UserResponse(UserBase):
    """
    Schema for the user response.

    This schema is used to return user information in the API response.
    It includes the user ID along with the basic user details.

    Attributes:
        id (int): The unique identifier of the user.
    """
    id: int

    class Config:
        """
        Configuration for the Pydantic model.

        Enables ORM mode to allow the model to be used with SQLAlchemy objects.
        """
        orm_mode = True  # Required for Pydantic to work with ORM models
