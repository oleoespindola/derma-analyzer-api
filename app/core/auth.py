from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt

from app.core.config import settings

bearer_scheme = HTTPBearer()

def create_token(user_id: str):
    expiration = datetime.now(timezone.utc) + timedelta(hours=1)
    payload = {'exp': expiration, 'sub': user_id}
    token = jwt.encode(payload, key=settings.API_KEY, algorithm=settings.ALGORITHM)
    return token

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    try:
        payload = jwt.decode(credentials.credentials, settings.API_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
