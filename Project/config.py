import os

# Secret key for CSRF protection, change it to a random value
SECRET_KEY = 'your_secret_key'

# Define the database URI
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False
