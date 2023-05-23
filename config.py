import os

# Base directory of the project
basedir = os.path.abspath(os.path.dirname(__file__))

def get_secret_key():
    with open('secret_key.txt', 'r') as file:
        secret_key = file.read().strip()
    return secret_key

class Config:
    # Secret key for protecting session data
    SECRET_KEY = get_secret_key()

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Other configuration options
    DEBUG = False
    API_KEY = 'your-api-key-goes-here'
    MAX_ITEMS_PER_PAGE = 10