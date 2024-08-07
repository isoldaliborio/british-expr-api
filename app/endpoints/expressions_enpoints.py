from flask import Blueprint
from flask import request, Response

bp = Blueprint("expressions", __name__)


@bp.route("/expressions/test")
def add_expression_route():
    return "ciao bella"


@bp.route('/add_tag/<restaurant>')
def add_tag(tag_name):
    tag = insert_tag(tag_name)
    return f"Inserted tag: {tag.id_tag}, {tag.tag}"
