from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app import schemas
from app.crud import user as user_crud
from app.schemas.user import UserResponse
from app.core.auth import verify_token

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db # Provides the session to the route
    finally:
        db.close()


@router.post("/", response_model=UserResponse)
def create_user(
        user: schemas.user.UserCreate, # User data (validated by Pydantic)
        db: Session = Depends(get_db), # Database session (injected)
        payload: dict = Depends(verify_token) # Checks if the email is already registered
    ):
    db_user = user_crud.get_user_by_email(db, email=user.email)     
    if db_user: # Checks if the email is already registered
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.create_user(db=db, user=user) # Creates the user if the email is unique