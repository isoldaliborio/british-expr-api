from flask import Blueprint
from flask import request, Response
from app.controllers.users_controller import add_new_user, get_user, update_user, delete_user, reactivate_user

bp = Blueprint("users", __name__)


@bp.route("/user", methods=["POST"])
def add_new_user_route() -> tuple[Response, int]:
    return add_new_user(request)

@bp.route("/user", methods=["GET"])
def get_user_route() -> tuple[Response, int]:
    return get_user(request)

@bp.route("/user", methods=["PUT"])
def update_user_route() -> tuple[Response, int]:
    return update_user(request)

@bp.route("/user", methods=["DELETE"])
def delete_user_route() -> tuple[Response, int]:
    return delete_user(request)

@bp.route("/user/reactivate", methods=["PUT"])
def reactivate_user_route() -> tuple[Response, int]:
    return reactivate_user(request)

