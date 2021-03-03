from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = 'pets'

    pet_id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.Text,
                           nullable=False)
    
    species = db.Column(db.Text,
                          nullable=False)
    
    photo_url = db.Column(db.Text,
                          nullable=True,
                          default='/static/images/sonic.png')
    
    age = db.Column(db.Integer,
                    nullable=True)
    
    notes = db.Column(db.Text,
                      nullable=True)
    
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)

