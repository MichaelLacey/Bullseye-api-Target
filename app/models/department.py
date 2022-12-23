from .db import db, environment, SCHEMA, add_prefix_for_prod

class Department(db.Model):
    __tablename__ = 'departments'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    image_url = db.Column(db.String(1000), nullable=False)

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'image_url': self.image_url
        }