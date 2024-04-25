from pydantic import BaseModel


# Pydantic model for creating a new user
class UserCreate(BaseModel):
    username: str
    password: str
