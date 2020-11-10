#create an internal item model.

from db import db

class ItemModel(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel') # like a Join db query


    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # SELECT * FROM items WHERE name=name. returns first row only
        #Returns item model object


    def save_to_db(self): # also known as upserting
        db.session.add(self) # session is a collection of objects that can be committed.
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()