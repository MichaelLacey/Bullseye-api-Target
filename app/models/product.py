from .db import db, environment, SCHEMA, add_prefix_for_prod

class Product(db.Model):
    __tablename__ = 'products'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}


    id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.integer, db.ForeignKey(add_prefix_for_prod('departments.id')), nullable=False)
    name = db.Column(db.String(40), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(100))