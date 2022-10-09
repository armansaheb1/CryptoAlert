from email.policy import default
from sqlalchemy import Integer, ForeignKey, String, Column
from . import db
from flask_login import UserMixin
from sqlalchemy.orm import backref



coin_exchange = db.Table('coin_exchange',
                    db.Column('coin_id', db.Integer, db.ForeignKey('coin.id')),
                    db.Column('exchange_id', db.Integer, db.ForeignKey('exchange.id'))
                    )



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    phone = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

class Alert(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    coin = db.Column(db.String(100))
    price = db.Column(db.String(100))
    exchange = db.Column(db.String(100))
    path = db.Column(db.Integer)
    status = db.Column(db.Integer, default= 0)
    user = db.Column(db.Integer, default= 0)
    
class Exchange(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100), unique=True)

class Coin(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100), unique=True)
    exchanges = db.relationship('Exchange', secondary=coin_exchange, backref='coins')
    
class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    user = db.Column(db.Integer, default= 0)
    name = db.Column(db.String(100))
    text = db.Column(db.String(1000))
    read = db.Column(db.Integer())
    aread = db.Column(db.Integer())
