import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
    SQLALCHEMY_DATABASE_URI = "sqlite:///attendance.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret")
    MAIL_SERVER = os.getenv("MAIL_SERVER", "smtp.gmail.com")
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")
    CELERY_BROKER_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    CELERY_RESULT_BACKEND = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    CACHE_TTL_STUDENT = 600    # 10 minutes
    CACHE_TTL_ADMIN = 300      # 5 minutes