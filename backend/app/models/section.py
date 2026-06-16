from ..extensions import db

class Section(db.Model):
    __tablename__ = "sections"
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey("courses.id"), nullable=False)
    section_name = db.Column(db.String(50), nullable=False)
    academic_year = db.Column(db.String(20))
    semester = db.Column(db.String(20))

    students = db.relationship("Student", backref="section", lazy=True)