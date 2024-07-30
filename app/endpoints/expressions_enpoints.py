from flask import Blueprint
from flask import request, Response
from app.controllers.expressions import add_expression


bp = Blueprint("expressions", __name__)


@bp.route("/admin/add")
def add_expression_route() -> tuple[Response, int]:
    return "ciao bella"
    # return add_expression(request)

