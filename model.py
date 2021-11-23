""""Model for saved drawing gallery."""
# from drawing import db
from flask_sqlalchemy import SQLAlchemy
from __init__ import create_app
# from flask_migrate import Migrate

db = SQLAlchemy()
# migrate = Migrate()

class Gallery(db.Model):
    """"Gallery for saved drawings."""

    __tablename__="gallery"

    img_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    img_name = db.Column(db.String)
    img_tags = db.Column(db.String)

    def __repr__(self):
        return f"Gallery img_id = {self.img_id}, img_name = {self.img_name}, img_tags = {self.img}"

def connect_to_db(flask_app, db_uri=None, echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///gallery"
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    print("Connected to the db!")

if __name__=='__main__':
    from server import app

    connect_to_db(app)