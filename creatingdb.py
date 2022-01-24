from flask_sqlalchemy import SQLAlchemy
from flask import Flask

application = Flask(__name__)
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///KupalovaDatabase.db'
database = SQLAlchemy(application) 


class Customer(database.Model):

    id = database.Column(database.Integer, primary_key=True)
    login = database.Column(database.String(80), unique=True, nullable=False)
    name = database.Column(database.String(80))
    password = database.Column(database.String(80), nullable=False)
    address = database.Column(database.String(80))
    registration_date = database.Column(database.DateTime, nullable=False)
    birthday = database.Column(database.Date)

    def __repr__(self):
        return f'{self.id}'


class Item(database.Model):

    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(80), unique=True, nullable=False)
    price = database.Column(database.Integer, nullable=False)
    category = database.Column(database.Integer, primary_key=True)
    number = database.Column(database.Integer)



class Order(database.Model):

    id = database.Column(database.Integer, primary_key=True)
    customer_id = database.Column(database.Integer, database.ForeignKey('customer.id'), nullable=False)
    costumer = database.relationship('Customer', backref=database.backref('activecostumer', lazy=False))
    in_total = database.Column(database.Integer, nullable=False)
    address = database.Column(database.String(80))
    order_date = database.Column(database.DateTime, nullable=False)

class ShoppingCart(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    customer_id = database.Column(database.Integer, database.ForeignKey('customer.id'), nullable=False)
    costumer = database.relationship('Customer', backref=database.backref('activecostumer', lazy=False))
    price = database.Column(database.Integer, nullable=False)
    item_id = database.Column(database.Integer, database.ForeignKey('item.id'), nullable=False)
    item = database.relationship('Item', backref=database.backref('activeitem', lazy=False))
    number = database.Column(database.Integer)

database.create_all()