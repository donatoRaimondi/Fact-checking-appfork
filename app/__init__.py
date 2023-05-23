from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database import db

# Create the Flask application object
app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

# Set the configuration options
app.config.from_object('config')

# Import the views module to register the routes
from app import routes