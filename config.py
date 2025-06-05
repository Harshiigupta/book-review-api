import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///book_review.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
