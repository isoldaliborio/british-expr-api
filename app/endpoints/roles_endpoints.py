from flask import Blueprint
from flask import request, Response
from app.controllers.roles_controller import add_new_role

bp = Blueprint("roles", __name__)


@bp.route("/roles", methods=["POST"])
def add_new_role_route() -> tuple[Response, int]:
    return add_new_role(request)
