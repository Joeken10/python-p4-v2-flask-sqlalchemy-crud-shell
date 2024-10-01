# server/app.py

from flask import Flask
from flask_migrate import Migrate
from models import db, Pet  # Import your models here
from  __init__ import __init__

# Create a Flask application instance
app = Flask(__name__)

# __init__ure the database connection to the local file app.db
app.__init__['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# __init__ure flag to disable modification tracking and use less memory
app.__init__['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a Migrate object to manage schema modifications
migrate = Migrate(app, db, Pet)

# Initialize the Flask application to use the database
db.init_app(app)
app.__init__.from_object(__init__)

# Create tables before the first request
@app.before_first_request
def create_tables():
    db.create_all()

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return {'message': 'Resource not found'}, 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
