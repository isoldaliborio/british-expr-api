import os
import sys
from pathlib import Path
from flask import Flask
from dotenv import load_dotenv

# Configure path
parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

from app.endpoints import expressions_enpoints
from app.models import db


# Initialize Flask app
app = Flask(__name__)

# Register blueprint endpoints
app.register_blueprint(expressions_enpoints.bp)

# Configure SQLAlchemy
isProd = os.getenv("ENV") == "prod"

if not isProd:
    load_dotenv(os.path.join(os.path.dirname(__file__), "..", "docker", ".env"))

DB_HOST = "db" if isProd else "localhost"
DB_PORT = "3306" if isProd else "5306"
MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

conn = f"mysql+pymysql://root:{MYSQL_ROOT_PASSWORD}@{DB_HOST}:{DB_PORT}/{MYSQL_DATABASE}"

print(conn)
app.config["SQLALCHEMY_DATABASE_URI"] = conn
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "brie"
db.init_app(app)


def insert_tag(tag_name):
    from app.models.expressions_models import Tag

    # Check if the tag already exists
    existing_tag = Tag.query.filter_by(tag=tag_name).first()
    if existing_tag:
        return existing_tag  # Return the existing tag

    # Create a new Tag object
    new_tag = Tag(tag=tag_name)

    # Add the new tag to the session
    db.session.add(new_tag)

    # Commit the session to persist the changes
    db.session.commit()

    return new_tag  # Return the newly created tag


# Insert a test tag
with app.app_context():
    tag = insert_tag("pub")
    print(f"Inserted tag: {tag.id_tag}, {tag.tag}")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
