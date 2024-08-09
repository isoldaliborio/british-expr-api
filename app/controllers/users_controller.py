from app.models.expressions_models import User

def add_new_user(db, first_name, last_name, email, password, role_id):
    """
    Add a new user to the database. If the user with the given email already exists, return the existing user.
    
    :param db: SQLAlchemy database session
    :param first_name: First name of the user
    :param last_name: Last name of the user
    :param email: Email of the user (must be unique)
    :param password: Password of the user (should be hashed before storing)
    :param role_id: ID of the role assigned to the user
    :return: The newly created or existing user
    """ 
    
    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return existing_user
    
    new_user = User(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,  # TODO: Password should be hashed before storing
        role_id=role_id
    )

    db.session.add(new_user)
    
    db.session.commit()
    
    return new_user 


def get_user(db, email):
    """
    Retrieve a user's information from the database using their email.
    
    :param db: SQLAlchemy database session
    :param email: Email of the user to retrieve
    :return: The user object if found, otherwise None
    """
    
    # Query the database for a user with the given email
    user = User.query.filter_by(email=email).first()
    
    # Return the user object if found, otherwise return None
    return user

def update_user(db, email, first_name=None, last_name=None, password=None, role_id=None):
    """
    Update a user's information in the database based on their email.
    
    :param db: SQLAlchemy database session
    :param email: Email of the user to update (used to identify the user)
    :param first_name: New first name (optional)
    :param last_name: New last name (optional)
    :param password: New password (optional, should be hashed before storing)
    :param role_id: New role ID (optional)
    :return: The updated user object if found and updated, otherwise None
    """
    
    # Query the database for the user with the given email
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return None  # User not found, return None
    
    # Update the user's information if new values are provided
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    if password:
        user.password = password  # Note: Password should be hashed before storing
    if role_id:
        user.role_id = role_id
    
    # Commit the session to persist the changes
    db.session.commit()
    
    return user  # Return the updated user object


def delete_user(db, email):
    """
    Delete a user from the database based on their email.
    
    :param db: SQLAlchemy database session
    :param email: Email of the user to delete (used to identify the user)
    :return: True if the user was deleted, False if the user was not found
    """
    
    # Query the database for the user with the given email
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return False  # User not found, return False
    
    # Delete the user from the session
    db.session.delete(user)
    
    # Commit the session to persist the changes
    db.session.commit()
    
    return True  # Return True to indicate successful deletion
