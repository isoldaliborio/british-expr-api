import bcrypt
from sqlalchemy.orm import class_mapper


def encrypt_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def check_password(password, hashed_password):
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)

# convert an SQLAlchemy object to a dictionary
def object_as_dict(obj):
    return {c.key: getattr(obj, c.key) for c in class_mapper(obj.__class__).columns}
