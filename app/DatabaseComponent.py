# Database Component
# from Shake import *
# from User import *
# from ingredients.Ingredient import *
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
import sqlalchemy as sa

from app import db

user_favorites_list = db.Table('user_favorites_list',
    db.Column('userID', db.Integer, db.ForeignKey('user.id')),
    db.Column('recipeID', db.Integer, db.ForeignKey('recipe_table.id'))
)

filter_table = db.Table('filter_table',
    # db.Column('recipe_table_id', db.Integer(), db.ForeignKey('recipe_table.id')),
    # db.Column('ingredients_table_id', db.Integer(), db.ForeignKey('ingredients_table.id'))
    db.Column('recipe_table_name', db.Integer(), db.ForeignKey('recipe_table.name')),
    db.Column('ingredients_table_name', db.Integer(), db.ForeignKey('ingredients_table.name'))
    )

class User(db.Model, UserMixin): ## creates the database table which stores the user login info
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(80))
    favorites = db.relationship('recipe_table', secondary=user_favorites_list, backref='hasFavorited')

    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, email={self.email}, password={self.password})'

    def __init__(self, name:str, email: str, password: str):
        """Create a new User object using the email address and hashing the
        plaintext password using Werkzeug.Security.
        """
        self.name = name
        self.email = email
        self.password = password

        
    def is_password_correct(self, password: str):
        return check_password_hash(self.password, password)

    def set_password(self, password: str):
        self.password = self._generate_password_hash(password)

    @staticmethod
    def _generate_password_hash(password):
        return generate_password_hash(password)




class recipe_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    calories = db.Column(db.String(100))
    fat = db.Column(db.String(100))
    sugar = db.Column(db.String(100))
    recipetext = db.Column(db.String(500))
    ingredients = db.relationship('ingredients_table', secondary=filter_table, backref='isIn')

    def __repr__(self):
        return f'Recipe(id={self.id}, name={self.name}, calories={self.calories}, fat={self.fat}, sugar={self.sugar}, recipetext={self.recipetext})'

class ingredients_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), primary_key=True)

    def __repr__(self):
        return f'Ingredient(id={self.id}, name={self.name})'
    
