from flask import jsonify
from flask import Request, Response
from app.services.users_service import encrypt_password, check_password, object_as_dict
from flask_jwt_extended import get_jwt_identity
from app.models.expressions_models import User
from app.models import db

def add_new_user(request: Request) -> tuple[Response, int]:

    data = request.get_json()
    email = data.get("email")
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify(message="That email already exists."), 204

    first_name = data.get("first_name")
    last_name = data.get("last_name")
    password = encrypt_password(data.get("password"))
    role_id = data.get("role_id")
    
    new_user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        role_id=role_id
    )

    db.session.add(new_user)
    
    try:
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 404

    return jsonify({"message": "User created successfully."}), 200


def get_user(request: Request) -> tuple[Response, int]:
    data = request.get_json()
    email = data.get("email")
    existing_user = User.query.filter_by(email=email).first()

    if not existing_user:
        return jsonify(message="email does not exist."), 404

    return jsonify(object_as_dict(existing_user)), 200


def update_user(request: Request) -> tuple[Response, int]:
   
    data = request.get_json()
    email = data.get("email")

    if not email:
        return jsonify(message="email not provided."), 204

    user = User.query.filter_by(email=email).first()
    
    if not user:
        return jsonify(message="User not found."), 404

    if data.get("first_name"):
        user.first_name = data.get("first_name")
    if data.get("last_name"):
        user.last_name = data.get("last_name")
    if data.get("password"):
        user.password = encrypt_password(data.get("password"))
    if data.get("role_id"):
        user.role_id = data.get("role_id")

    db.session.commit()
    
    return jsonify(object_as_dict(user)), 200 


def delete_user(request: Request) -> tuple[Response, int]:
    data = request.get_json()
    email = data.get("email")
    
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return jsonify(message="User not found."), 404
    
    user.active = False
    
    db.session.commit()
    
    return jsonify(message="User deleted successfully."), 200


def reactivate_user(request: Request) -> tuple[Response, int]:
    data = request.get_json()
    email = data.get("email")
    
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return jsonify(message="User not found."), 404
    
    user.active = True
    
    db.session.commit()
    
    return jsonify(message="User reactivated successfully."), 200
