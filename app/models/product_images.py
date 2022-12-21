from .db import db, environment, SCHEMA, add_prefix_for_prod


class Product_Image(db.Model):
    __tablename__ = 'product_images'


if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')), nullable=False)
    image_url = db.Column(db.String(1000), nullable=False)
