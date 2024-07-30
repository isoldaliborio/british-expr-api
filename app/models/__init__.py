from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .expressions_models import Expressions, Tag, TagsExpressions
