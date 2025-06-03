from pydantic import BaseModel

class TokenRequest(BaseModel):
    secret: str
