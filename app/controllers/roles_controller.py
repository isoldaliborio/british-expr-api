from flask import jsonify
from flask import Request, Response
from app.models.expressions_models import Role
from app.services.users_service import object_as_dict
from app.models import db

def add_new_role(request: Request) -> tuple[Response, int]:
    data = request.get_json()
    name = data.get("name")
    existing_role = Role.query.filter_by(name=name).first()
    if existing_role:
        return jsonify(message="That role already exists."), 204


    new_role = Role(
        name=name
    )

    db.session.add(new_role)

    db.session.commit()

    return jsonify(object_as_dict(new_role)), 200 

