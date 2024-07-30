from flask import jsonify, Request, Response
from app.models import Expressions, Tags, TagsExpressions
# from app.app import db


def add_expression(request: Request) -> tuple[Response, int]:
    data = request.get_json()

    expression_text = data.get("expression")
    meaning = data.get("meaning")
    uses_example = data.get("uses_example")
    context = data.get("context")
    tag_ids = data.get("tags")
    tag = Tag.query.get(tag_id)

    if not expression_text:
        return jsonify({'error': 'Expression text is required'}), 400

    # Check if the expression already exists
    existing_expression = Expressions.query.filter_by(expression=expression_text).first()

    if existing_expression:
        return jsonify({'error': 'Expression already exists'}), 400

    # Handle tags
    tags = []
    if tag_names:
        for tag_name in tag_names:
            # Check if the tag already exists
            tag = Tag.query.filter_by(tag=tag_name).first()
            if not tag:
                # Create a new tag if it does not exist
                tag = Tag(tag=tag_name)
                db.session.add(tag)
            tags.append(tag)

    new_expression = Expressions(
        expression = expression_text,
        meaning = meaning,
        uses_example = uses_example,
        context = context,
   )

           # Associate the tags with the new expression
    new_expression.tags = tags


       # Add and commit to the database
    try:
        db.session.add(new_expression)
        db.session.commit()

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': 'Expression added successfully', 'expression_id': new_expression.id_exp}), 201






    #    # If there are tags, associate them with the new expression
    # if tag_ids:
    #     tags = Tag.query.filter(Tag.id_tag.in_(tag_ids)).all()
    #     new_expression.tags = tags
     



