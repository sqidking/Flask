from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Tell Flask where application is and configure it.
application = Flask(__name__)  # Tell Flask where application is
application.config.from_object(Config)  # Configure application from file
db = SQLAlchemy(application)  # Database
migrate = Migrate(application, db)  # Migration Engine for DB

# This is placed below to avoid circular dependencies (See Flask Mega Tutorial Part 1)
from app import routes, models