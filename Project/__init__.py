from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)
app.config.from_object('config')

# Initialize SQLAlchemy
db = SQLAlchemy(app)

from app import routes
