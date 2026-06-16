from ..extensions import db
from datetime import datetime

class Course(db.Model):
    __tablename__ = "courses"
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    course_code = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    sections = db.relationship("Section", backref="course", lazy=True, cascade="all, delete-orphan")
    attendances = db.relationship("Attendance", backref="course", lazy=True)