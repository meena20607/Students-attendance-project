from ..extensions import db
from datetime import datetime

class Attendance(db.Model):
    __tablename__ = "attendances"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(10), nullable=False)  # present / absent / leave
    marked_by = db.Column(db.Integer, db.ForeignKey("admins.id"), nullable=True)
    remarks = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)