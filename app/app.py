import os
from flask import Flask
from os.path import join, dirname, abspath
# from .endpoints.pick_random_expression_endpoint import pick_random_expression_route

app = Flask(__name__)

# Register blueprint endpoints
# app.register_blueprint(pick_random_expression_route.bp)

# Database config
MYSQL_ROOT_PASSWORD = os.environ["MYSQL_ROOT_PASSWORD"]
MYSQL_DATABASE = os.environ["MYSQL_DATABASE"]
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://root:{MYSQL_ROOT_PASSWORD}@db/{MYSQL_DATABASE}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "brie"
# db.init_app(app)


@app.route('/')
def index():
    return 'Welcome to the British Expressions Web App!'
#
#
# @app.route('/expressions')
# def get_expressions():
#     # Functionality to retrieve and return expressions from the database
#     return 'List of British expressions'


if __name__ == '__main__':
    app.run(debug=True)