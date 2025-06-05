from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Derma Analyzer API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = 'A Derma Analyzer API é uma aplicação web que utiliza técnicas de aprendizado de máquina para analisar imagens de pele e detectar possíveis casos de melanoma.'
    API_KEY: str
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"


settings = Settings()