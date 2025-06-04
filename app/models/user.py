from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.db.database import Base # Gets a database connection

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

class Image_Analysis(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String, nullable=False)
    analysis_result = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    user_feedback = Column(String, nullable=True)
    feedback_timestamp = Column(DateTime, nullable=True)