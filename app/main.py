import os
import sys
from pathlib import Path
from flask import Flask
from dotenv import load_dotenv

# Configure path
parent_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(parent_dir))

from app.endpoints import expressions_enpoints, users_endpoints, roles_endpoints, expressions_enpoints

from app.models import db

# Testing
from app.controllers.users_controller import add_new_user
from app.controllers.roles_controller import add_new_role
from app.controllers.expressions_controller import add_new_expression

# Initialize Flask app
app = Flask(__name__)

# Register blueprint endpoints
app.register_blueprint(expressions_enpoints.bp)
app.register_blueprint(users_endpoints.bp)
app.register_blueprint(roles_endpoints.bp)

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


# with app.app_context():
#     insert_role(db, "admin")
#     # add_new_user(db, "Isolda", "Liborio", "isolda@test.com", "1234", 1)
#     # add_new_expression(db, "abc", "aabbcc", 1)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

