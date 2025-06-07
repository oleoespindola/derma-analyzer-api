from pydantic import BaseModel, EmailStr

class AuthRequest(BaseModel):
    email: str
    password: str

class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    sub: int
    access_token: str
    token_type: str = "bearer"

    class Config:
        orm_mode = True # converts ORM (SQLAlchemy) directly to JSON
