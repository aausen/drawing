""""Model for saved drawing gallery."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Gallery(db.Model):
    """"Gallery for saved drawings."""

    __tablename__="gallery"

    img_id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    img_name = db.Column(db.String)
    img_tags = db.Column(db.String)

    def __repr__(self):
        return f"Gallery img_id = {self.img_id}, img_name = {self.img_name}, img_tags = {self.img}"

def connect_to_db(flask_app, db_uri="postgresql:///gallery", echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFCATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")

if __name__=='__main__':
    from server import app

    connect_to_db(app)