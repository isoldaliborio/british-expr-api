from flask import jsonify
from flask import Request, Response
from app.models.expressions_models import Expression, Example
from app.services.users_service import object_as_dict
import datetime;
from app.models import db

def add_new_expression(request: Request) -> tuple[Response, int]:
    
    data = request.get_json()
    expression = data.get("expression")
    existing_expression = Expression.query.filter_by(expression=expression).first()
    if existing_expression:
        return jsonify(message="That expression already exists."), 204
    
    meaning = data.get("meaning")
    examples = data.get("examples")
    user_id = data.get("user_id")

    ct = datetime.datetime.now()
    new_expression = Expression(
        expression=expression,
        meaning=meaning,
        created_at=ct,
        modified_at=ct,
        user_id=user_id
    )   

    db.session.add(new_expression)
    db.session.commit()
    
    expression_id = new_expression.expression_id

    add_examples(expression_id, examples)
    
     #TODO: get the id of the new expression then create a for loop for each example.

    return jsonify(object_as_dict(new_expression)), 200

def add_examples(expression_id, examples):
    for example in examples:
        new_example = Example(
            expressions_expression_id=expression_id,
            example=example
        )
        db.session.add(new_example)
    db.session.commit()
    return 


