from flask import Flask

# Create the Flask application object
app = Flask(__name__)

# Set the configuration options
#app.config.from_object('config')

# Import the views module to register the routes
from app import routes