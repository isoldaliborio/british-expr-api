from flask import Blueprint
from flask import request, Response
from app.controllers.expressions_controller import add_new_expression, update_expression

bp = Blueprint("expressions", __name__)


@bp.route("/expressions/", methods=["POST"])
def add_new_expression_route():
    return add_new_expression(request)

@bp.route("/expressions/", methods=["PUT"])
def update_expression_route():
    return update_expression(request)
