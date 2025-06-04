from datetime import datetime
import os

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from app.db.database import SessionLocal
from app import schemas
from app.crud import user as user_crud
from app.models.keras_model import predict_image
from app.schemas.user import UserResponse, AuthRequest
from app.core.auth import verify_token
from app.core.security import verify_password

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

os.makedirs("app/db/images", exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db # Provides the session to the route
    finally:
        db.close()


@router.post("/new", response_model=UserResponse)
def create_user(
        user: schemas.user.UserCreate, # User data (validated by Pydantic)
        db: Session = Depends(get_db), # Database session (injected)
        payload: dict = Depends(verify_token) # Checks if the email is already registered
    ):
    db_user = user_crud.get_user_by_email(db, email=user.email)     
    if db_user: # Checks if the email is already registered
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_crud.new_user(db=db, user=user) # Creates the user if the email is unique


@router.post("/auth", response_model=UserResponse)
def login(
        auth: AuthRequest, # User data (validated by Pydantic)
        db: Session = Depends(get_db), # Database session (injected)
        payload: dict = Depends(verify_token) # Checks if the email is already registered
    ):
    """
    Authenticates a user by verifying the provided email and password.

    Args:
        email (str): The email of the user attempting to log in.
        password (str): The password of the user attempting to log in.
        db (Session): The database session used for querying user information.
        payload (dict): The token payload obtained from verifying the authorization token.

    Raises:
        HTTPException: If the email is not registered or if the password is invalid.

    Returns:
        UserResponse: The authenticated user's information.
    """

    db_user = user_crud.get_user_by_email(db, email=auth.email)     
    if not db_user: # Checks if the email is already registered
        raise HTTPException(status_code=400, detail="Email not registered")
    if not verify_password(plain_password=auth.password, hashed_password=db_user.password):
        raise HTTPException(status_code=400, detail="Invalid password")
    return db_user

@router.post("/predict", response_model=UserResponse)
async def user_predict(
        user_auth: UserResponse,
        db: Session = Depends(get_db),
        file: UploadFile = File(...),
        payload: dict = Depends(verify_token)
    ):
    contents = await file.read()
    prediction = predict_image(contents)
    image_url = f"app/db/images/{user_auth.id} - {datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.png"
    with open(image_url, "wb") as buffer:
        buffer.write(contents)
    image_Analysis = user_crud.save_prediction(
        db=db, 
        id=user_auth.id, 
        analysis_result=prediction, 
        image_url=image_url
    )
    return JSONResponse(image_Analysis)