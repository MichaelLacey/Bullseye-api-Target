from .db import db, environment, SCHEMA, add_prefix_for_prod

Cart_Product = db.Table(
    'cart_products',
    db.Column('product_id', db.Integer, db.ForeignKey(add_prefix_for_prod('products.id'))),
    db.Column('cart_id', db.Integer, db.ForeignKey(add_prefix_for_prod('carts.id')))
)

if environment == 'production':
    members.schema = SCHEMA

