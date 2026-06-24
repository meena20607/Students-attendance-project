
from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models.course import Course

courses_bp = Blueprint("courses", __name__)

@courses_bp.route("/", methods=["POST"])
def create_course():

    data = request.get_json()

    course = Course(
        course_name=data["course_name"],
        course_code=data["course_code"],
        description=data.get("description", "")
    )

    db.session.add(course)
    db.session.commit()

    return jsonify({
        "message": "Course created successfully"
    }), 201

@courses_bp.route("/", methods=["GET"])
def get_courses():

    courses = Course.query.all()

    result = []

    for c in courses:
        result.append({
            "id": c.id,
            "course_name": c.course_name,
            "course_code": c.course_code,
            "description": c.description
        })

    return jsonify(result)



@courses_bp.route("/<int:id>", methods=["PUT"])
def update_course(id):

    course = Course.query.get_or_404(id)

    data = request.get_json()

    course.course_name = data["course_name"]
    course.course_code = data["course_code"]
    course.description = data["description"]

    db.session.commit()

    return jsonify({
        "message": "Course updated successfully"
    })

@courses_bp.route("/<int:id>", methods=["DELETE"])
def delete_course(id):

    course = Course.query.get_or_404(id)

    db.session.delete(course)
    db.session.commit()

    return jsonify({
        "message": "Course deleted successfully"
    })