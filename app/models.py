from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash


db = SQLAlchemy()

class My5(db.Model):
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)

# create our Models based off of our ERD
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    team = db.relationship(
        'Pokemon',
        secondary = 'my5',
        backref= 'users',        
        lazy='dynamic'
    )

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)


class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    ability = db.Column(db.String(150))
    img_url = db.Column(db.String(300))
    hp = db.Column(db.Integer)
    attack = db.Column(db.Integer)
    defense = db.Column(db.Integer)

    def __init__(self, name, ability, img_url, hp, attack, defense):
        self.img_url = img_url
        self.name = name
        self.hp = hp
        self.ability = ability
        self.attack = attack
        self.defense = defense