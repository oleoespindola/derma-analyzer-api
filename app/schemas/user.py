# This file does not connect to the database; it only handles API data flow; Input/Output

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int

    class Config:
        orm_mode = True # converts ORM (SQLAlchemy) directly to JSON
