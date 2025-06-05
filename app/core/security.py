from fastapi import HTTPException
from passlib.context import CryptContext

# If "sha256" were ever deprecated, passlib would warn but still verify old hashes.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    if not pwd_context.verify(plain_password, hashed_password):
        raise HTTPException(status_code=401, detail="Invalid password")
