from .db import db, environment, SCHEMA, add_prefix_for_prod

Cart_Product = db.Table(
    'cart_products',
    db.Column('product_id', db.Integer, db.ForeignKey(add_prefix_for_prod('products.id'))),
    db.Column('user_id', db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))
)



if environment == 'production':
    Cart_Product.schema = SCHEMA

