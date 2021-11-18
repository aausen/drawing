"""CRUD operations."""

from abc import abstractproperty
from model import Gallery, db, connect_to_db

def create_image(img_name, img_tags):
    """Create and return a new image."""

    image = Gallery(img_name = img_name,
                    img_tags = img_tags)

    db.session.add(image)
    db.session.commit()

    return image

def get_all_images():
    """Get all images from the database."""

    return Gallery.query.all()

def delete_image_from_db(img_id):
    """Delete an image from the database."""

    del_image = Gallery.query.filter(Gallery.img_id == img_id).first()
    db.session.delete(del_image)
    db.session.commit()

if __name__=='__main__':
    from server import app
    connect_to_db(app)