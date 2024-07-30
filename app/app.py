import os
from flask import Flask
from os.path import join
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
from endpoints import expressions_enpoints

# Load environment variables from .env file
dotenv_path = join(os.path.dirname(__file__), '..', 'docker', '.env')
load_dotenv(dotenv_path)

MYSQL_ROOT_PASSWORD = os.getenv("MYSQL_ROOT_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
DB_HOST = "db" if os.getenv("ENV") else "localhost"
DB_PORT = "3306" if os.getenv("ENV") else "5306"

# Initialize Flask app
app = Flask(__name__)

# Register blueprint endpoints
app.register_blueprint(expressions_enpoints.bp)

# Configure SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://root:{MYSQL_ROOT_PASSWORD}@{DB_HOST}:{DB_PORT}/{MYSQL_DATABASE}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "brie"

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the function to test database connection
def test_db_connection():
    with app.app_context():
        try:
            # Attempt to connect to the database
            with db.engine.connect() as connection:
                print("Database connection successful!")
        except OperationalError as e:
            print(f"Database connection failed: {e}")

@app.route('/')
def index():
    return 'Welcome to the British Expressions Web App, lov!'

if __name__ == '__main__':
    test_db_connection()
    app.run(host='0.0.0.0', port=8080, debug=True)
