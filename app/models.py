from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

my5 = db.Table('my5',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('pokemon_id', db.Integer, db.ForeignKey('pokemon.id')),
)

# create our Models based off of our ERD
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    team = db.relationship(
        'Pokemon',
        secondary = my5,
        backref= 'users',        
        lazy='dynamic'
    )

    def __init__(self, username, first_name, last_name,  email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = generate_password_hash(password)



class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    poke_img = db.Column(db.String(300))
    name = db.Column(db.String(50), unique = True)
    ability = db.Column(db.String(50))
    hp_stat = db.Column(db.Integer)
    atk_stat = db.Column(db.Integer)
    def_stat = db.Column(db.Integer)
    

    def __init__(self, poke_img, name, ability, hp_stat, atk_stat, def_stat):
        self.poke_img = poke_img
        self.name = name
        self.ability = ability
        self.hp_stat = hp_stat
        self.atk_stat = atk_stat
        self.def_stat = def_stat

