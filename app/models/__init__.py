from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


from .expressions_models import Category
from .expressions_models import UserRole
from .expressions_models import User
from .expressions_models import Words
from .expressions_models import Content

