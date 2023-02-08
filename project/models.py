from datetime import datetime
from flask_marshmallow import Marshmallow
from marshmallow import Schema, fields, validate
from.import app,db
import uuid
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
   
    def __repr__(self):
        return '<User %r>' % str(self.id)




class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text)
    qty = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(500))
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return '<Product %r>' % self.name



class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'password')


user_schema = UserSchema()
users_schema = UserSchema(many=True)