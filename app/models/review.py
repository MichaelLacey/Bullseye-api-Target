from .db import db, environment, SCHEMA, add_prefix_for_prod

class Review(db.Model):
    __tablename__ = 'reviews'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('products.id')), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('users.id')), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text(), nullable=False)

    review_to_product = db.relationship('Product', backref='reviews')


    def to_dict(self):
        return {
            'id':self.id,
            'product_id':self.product_id,
            'user_id': self.user_id,
            'rating': self.rating,
            'comment': self.comment
        }