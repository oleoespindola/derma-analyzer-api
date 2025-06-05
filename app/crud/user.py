from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User, Image_Analysis
from app.schemas.user import UserCreate, AuthRequest
from app.core import security, auth

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def new_user(db: Session, user: UserCreate):
    db_user = get_user_by_email(db=db, email=user.email)
    if db_user: # Checks if the email is already registered
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = User(
        name=user.name,
        email=user.email,
        password=security.hash_password(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    token = auth.create_token(str(db_user.id))
    return db_user, token

def user_auth(db: Session, user: AuthRequest):
    db_user = get_user_by_email(db=db, email=user.email)
    if not db_user:
        raise HTTPException(status_code=401, detail="Email not found")
    security.verify_password(plain_password=user.password, hashed_password=db_user.password)
    token = auth.create_token(str(db_user.id))
    return db_user, token


def save_prediction(db: Session, id: int, analysis_result, image_url: str):
    image_Analysis = Image_Analysis(
        id=id,
        analysis_result=analysis_result,
        image_url=image_url
    )
    db.add(image_Analysis)
    db.commit()
    db.refresh(image_Analysis)
    return image_Analysis

def prediction_feedback(db: Session, image_Analysis: Image_Analysis, user_feedback: str, feedback_timestamp: str):
    image_Analysis(
        user_feedback=user_feedback,
        feedback_timestamp=datetime.now()
    )
    db.merge(image_Analysis)
    db.commit()
    db.refresh(image_Analysis)
    return image_Analysis