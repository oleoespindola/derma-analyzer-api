from sqlalchemy import Column, Integer, String, DateTime, Boolean, Numeric 
from sqlalchemy import ForeignKey
from datetime import datetime

from app.db.database import Base # Gets a database connection

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)

class Image_Analysis(Base):
    __tablename__ = "image_analysis"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    image_url = Column(String, nullable=False)
    image_predict = Column(Numeric(1,10), nullable=False)
    created_at = Column(DateTime, default=datetime.now())
    user_feedback = Column(Boolean, nullable=True)
    feedback_timestamp = Column(DateTime, nullable=True)