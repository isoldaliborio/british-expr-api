from . import db

# Define the Roles model
class Roles(db.Model):
    __tablename__ = "roles"
    __table_args__ = {"schema": "british_expressions"}  # Specify the schema name

    role_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)

# Define the Users model
class Users(db.Model):
    __tablename__ = "users"
    __table_args__ = (
        db.UniqueConstraint("user_id", name="user_id_UNIQUE"),
        db.UniqueConstraint("email", name="email_UNIQUE"),
        {"schema": "british_expressions"}
    )  # Specify the schema name and unique constraints

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey("british_expressions.roles.role_id"), nullable=False)


# Define the Examples model
class Examples(db.Model):
    __tablename__ = "examples"
    __table_args__ = {"schema": "british_expressions"}  # Specify the schema name

    example_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    example = db.Column(db.Text, nullable=False)

# Define the Expressions model
class Expressions(db.Model):
    __tablename__ = "expressions"
    __table_args__ = (
        db.UniqueConstraint("expression_id", name="id_exp_UNIQUE"),
        {"schema": "british_expressions"}
    )  # Specify the schema name and unique constraint

    expression_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    expression = db.Column(db.String(200), nullable=False)
    meaning = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False)
    modified_at = db.Column(db.TIMESTAMP, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("british_expressions.users.user_id"), nullable=False)
    example_id = db.Column(db.Integer, db.ForeignKey("british_expressions.examples.example_id"), nullable=False)

    # Relationship to tags via a secondary table
    tags = db.relationship("Tags", secondary="british_expressions.user_tags", back_populates="expressions")

    # Relationship to categories via a secondary table
    categories = db.relationship("Categories", secondary="british_expressions.categories_expressions", back_populates="expressions")

# Define the Categories model
class Categories(db.Model):
    __tablename__ = "categories"
    __table_args__ = {"schema": "british_expressions"}  # Specify the schema name

    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    # Relationship to expressions via a secondary table
    expressions = db.relationship("Expressions", secondary="british_expressions.categories_expressions", back_populates="categories")

# Define the CategoriesExpressions association table
class CategoriesExpressions(db.Model):
    __tablename__ = "categories_expressions"
    __table_args__ = {"schema": "british_expressions"}  # Specify the schema name

    category_expression_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    expression_id = db.Column(db.Integer, db.ForeignKey("british_expressions.expressions.expression_id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("british_expressions.categories.category_id"), nullable=False)

# Define the Tags model
class Tags(db.Model):
    __tablename__ = "tags"
    __table_args__ = {"schema": "british_expressions"}  # Specify the schema name

    tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)

    # Relationship to expressions via a secondary table
    expressions = db.relationship("Expressions", secondary="british_expressions.user_tags", back_populates="tags")

# Define the UserTags association table
class UserTags(db.Model):
    __tablename__ = "user_tags"
    __table_args__ = {"schema": "british_expressions"}  # Specify the schema name

    expression_id = db.Column(db.Integer, db.ForeignKey("british_expressions.expressions.expression_id"), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey("british_expressions.tags.tag_id"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("british_expressions.users.user_id"), primary_key=True)

# Define the Favorites association table
class Favorites(db.Model):
    __tablename__ = "favorites"
    __table_args__ = {"schema": "british_expressions"}  # Specify the schema name

    expression_id = db.Column(db.Integer, db.ForeignKey("british_expressions.expressions.expression_id"), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("british_expressions.users.user_id"), primary_key=True)
