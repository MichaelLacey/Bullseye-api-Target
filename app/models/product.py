from .db import db, environment, SCHEMA, add_prefix_for_prod
from .cart_product import Cart_Product

class Product(db.Model):
    __tablename__ = 'products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod('departments.id')), nullable=False)
    name = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text)
    image_url1 = db.Column(db.String(1000))
    image_url2 = db.Column(db.String(1000))
    image_url3 = db.Column(db.String(1000))
    image_url4 = db.Column(db.String(1000))
    
    department_relationship = db.relationship('Department', backref='products')
    users = db.relationship(
        "User",
        secondary=Cart_Product,
        back_populates="products"
    )
    
    def to_dict(self):
        return {
            'id':self.id,
            'department_id':self.department_id,
            'name':self.name,
            'price': self.price,
            'description': self.description,
            'image_url1': self.image_url1,
            'image_url2': self.image_url2,
            'image_url3': self.image_url3,
            'image_url4': self.image_url4,
        }