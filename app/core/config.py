from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Derma Analyzer API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = '-----'
    SECRET_KEY: str
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()