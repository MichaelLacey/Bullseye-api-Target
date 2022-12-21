from .db import db, environment, SCHEMA, add_prefix_for_prod

Cart_Product = db.Table(
    'cart_products',
    db.Column(db.Integer, primary_key=True),
    db.Column('product_id', db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')))
    db.Column('cart_id', db.Integer, db.ForeignKey(add_prefix_for_prod('carts.id')))
)

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

