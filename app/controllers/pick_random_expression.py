from flask import jsonify, Request, Response
# from app.models import Category, Product, db
# from numpy import random


def pick_radom_expression(request: Request) -> tuple[Response, int]:
    # random_id = random.randint(100)
    data = request.get_json()
    product_by_id=data.get("id")
    return "teste"


