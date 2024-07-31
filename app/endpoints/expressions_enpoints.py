from flask import Blueprint
from flask import request, Response

bp = Blueprint("expressions", __name__)


@bp.route("/expressions/test")
def add_expression_route():
    return "ciao bella"
