from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    """
    Base schema for user information.

    This schema serves as a base for other user-related schemas.
    It includes the common attributes shared by multiple user actions.

    Attributes:
        username (str): The unique username of the user.
        email (EmailStr): The email address of the user.
    """
    id: int = Field(..., description="The unique identifier of the user.")
    username: str = Field(..., min_length=3, max_length=50, description="The unique username of the user.")
    email: EmailStr = Field(..., description="The email address of the user. Must be a valid email format.")
    password: str = Field(..., min_length=6, description="The password for the new user. Minimum length of 6 characters.")


class UserCreate(UserBase):
    """
    Schema for creating a new user.

    This schema is used to validate the request body when creating a new user.
    It extends the UserBase schema and includes the password attribute.

    Attributes:
        password (str): The password for the new user. Required during user registration.
    """
    id: int = Field(..., description="The unique identifier of the user.")
    username: str = Field(..., min_length=3, max_length=50, description="The unique username of the user.")
    email: EmailStr = Field(..., description="The email address of the user. Must be a valid email format.")
    password: str = Field(..., min_length=6, description="The password for the new user. Minimum length of 6 characters.")


class UserResponse(UserBase):
    """
    Schema for the user response.

    This schema is used to return user information in the API response.
    It includes the user ID along with the basic user details.

    Attributes:
        id (int): The unique identifier of the user.
    """
    id: int = Field(..., description="The unique identifier of the user.")

    class Config:
        """
        Configuration for the Pydantic model.

        Enables ORM mode to allow the model to be used with SQLAlchemy objects.
        """
        orm_mode = True  # Required for Pydantic to work with ORM models
        from_attributes = True  # Improved compatibility with SQLAlchemy models
