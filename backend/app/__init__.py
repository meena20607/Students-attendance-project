from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db, jwt, mail, celery
from .routes.courses import courses_bp
from .models import *

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, origins=["http://localhost:3000"])
    db.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)

    # Configure Celery
    celery.conf.update(app.config)

    # Register blueprints
    from .routes.auth import auth_bp
    # from .routes.courses import courses_bp
  

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(courses_bp, url_prefix="/api/courses")
    # app.register_blueprint(sections_bp, url_prefix="/api/sections")
    # app.register_blueprint(students_bp, url_prefix="/api/students")
    # app.register_blueprint(attendance_bp, url_prefix="/api/attendance")
    # app.register_blueprint(leave_bp, url_prefix="/api/leave")
    # app.register_blueprint(analytics_bp, url_prefix="/api/analytics")

    return app


