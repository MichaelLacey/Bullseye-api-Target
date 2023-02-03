from .db import db, environment, SCHEMA, add_prefix_for_prod


class Wishlist(db.Model):

    __tablename__ = 'wishlists'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')))
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')))

    wishlist_to_product = db.relationship('Product', backref='wishlists')
    wishlist_to_user = db.relationship('User', backref='wishlists')

    def to_dict(self):
        return {
            'id':self.id,
            'product_id':self.product_id,
            'user_id': self.user_id
        }