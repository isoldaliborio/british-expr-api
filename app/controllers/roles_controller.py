from app.models.expressions_models import Role

def insert_role(db, role_name):

    # Check if the role already exists
    existing_role = Role.query.filter_by(name=role_name).first()
    if existing_role:
        return existing_role  # Return the existing role

    # Create a new Role object
    new_role = Role(name=role_name)

    # Add the new role to the session
    db.session.add(new_role)

    # Commit the session to persist the changes
    db.session.commit()

    return new_role  # Return the newly created role


def delete_role(db, role_name):
    # Check if the role already exists
    role_to_delete = Role.query.filter_by(name=role_name).first()
    if not role_to_delete:
        return False  

    # Delete the new role to the session
    db.session.delete(role_to_delete)

    # Commit the session to persist the changes
    db.session.commit()

    return True
