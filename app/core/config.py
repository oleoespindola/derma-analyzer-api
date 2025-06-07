from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Derma Analyzer API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = 'A Derma Analyzer API é uma aplicação web que utiliza técnicas de aprendizado de máquina para analisar imagens de pele e detectar possíveis casos de melanoma.'
    ALGORITHM: str = "HS256"
    API_KEY: str
    DB_USER: str
    DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    CLOUDINARY_NAME: str
    CLOUDINARY_API: str
    CLOUDINARY_API_KEY: str
    
    class Config:
        env_file = ".env"


settings = Settings()