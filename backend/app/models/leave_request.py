from ..extensions import db
from datetime import datetime

class LeaveRequest(db.Model):
    __tablename__ = "leave_requests"
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("students.id"), nullable=False)
    from_date = db.Column(db.Date, nullable=False)
    to_date = db.Column(db.Date, nullable=False)
    reason = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(10), default="pending")  # pending / approved / rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)