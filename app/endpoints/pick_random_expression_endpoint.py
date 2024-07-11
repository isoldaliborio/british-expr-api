from flask import Blueprint
from flask import request, Response
from app.controllers.pick_random_expression import pick_radom_expression


bp = Blueprint("expression", __name__)


@bp.route("/expression")
def pick_random_expression_route() -> tuple[Response, int]:
    return pick_radom_expression(request)


@bp.route("/expression")
def search_expression_route() -> tuple[Response, int]:
    return search_radom_expression(request)


@bp.route("/expression")
def find_expression_by_tag_route() -> tuple[Response, int]:
    return find_expression_by_tag(request)
