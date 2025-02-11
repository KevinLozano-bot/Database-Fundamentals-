from pydantic import BaseModel, ConfigDict 

class UserCreate(BaseModel):
    email: str
    password: str

class UserResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    id: int
    username: str
    email: str

    #class Config:
        #arbitrary_types_allowed = True