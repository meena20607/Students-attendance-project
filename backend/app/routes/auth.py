from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.extensions import db
from app.models.admin import Admin
from app.models.student import Student

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/admin/login", methods=["POST"])
def admin_login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    admin = Admin.query.filter_by(email=email).first()

    if not admin or not admin.check_password(password):
        return jsonify({"message": "Invalid credentials"}), 401

    token = create_access_token(
        identity=str(admin.id),
        additional_claims={"role": "admin"}
    )

    return jsonify({
        "token": token,
        "role": "admin"
    }), 200

@auth_bp.route("/student/login", methods=["POST"])
def student_login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    student = Student.query.filter_by(email=email).first()

    if not student or not student.check_password(password):
        return jsonify({"message": "Invalid credentials"}), 401

    token = create_access_token(
        identity=str(student.id),
        additional_claims={"role": "student"}
    )

    return jsonify({
        "token": token,
        "role": "student"
    }), 200

from flask_jwt_extended import jwt_required, get_jwt

@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def me():

    claims = get_jwt()

    return jsonify({
        "message": "Token Valid",
        "role": claims["role"]
    })


