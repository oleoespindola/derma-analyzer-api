from fastapi import HTTPException, APIRouter
from fastapi.responses import JSONResponse

from app.core.auth import create_token
from app.schemas.token import TokenRequest
from app.core.config import settings

router = APIRouter(
    tags=["Auth"]
)

@router.post("/token")
async def generate_token(payload: TokenRequest):
    if payload.secret != settings.SECRET_KEY:
        raise HTTPException(status_code=401, detail="Invalid secret key")
    token = create_token()
    return JSONResponse(content={'access_token': token, 'token_type': "bearer"})