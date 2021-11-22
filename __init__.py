import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
DATABASE_URL = os.environ['DATABASE_URL']
def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_key',
        SQLALCHEMY_DATABASE_URI = DATABASE_URL or "postgresql:///gallery",
        SQLALCHEMY_TRACK_MODIFICATIONS = False
    )
   
    db.init_app(app)
    migrate.init_app(app, db)

    from . import model

    return app