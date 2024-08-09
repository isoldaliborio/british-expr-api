from app.models.expressions_models import Expression
import datetime;

def add_new_expression(db, expression, meaning, user_id):
    
    """
    Add a new expression to the database. If the expression with the given id already exists, return the existing expression.
    
    :param db: SQLAlchemy database session
    :param expressione: Expresssion to be added
    :param mening: Meaning of the expression
    :param user_id: id of the user
    :return: The newly created or existing expression
    """ 
    
    existing_expression = User.query.filter_by(expression=expression).first()
    if existing_expression:
        return existing_expression
    
    ct = datetime.datetime.now()
    new_expression = User(
        expression=expression,
        meaning=meaning,
        created_at=ct,
        modified_at=ct,
        user_id=user_id
    )

    db.session.add(new_expression)
    
    db.session.commit()
    
    return new_expression 