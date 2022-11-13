# Database Component
# from Shake import *
# from User import *
# from ingredients.Ingredient import *
from flask_login import UserMixin
import sqlalchemy as sa

from app import db

class User(db.Model, UserMixin): ## creates the database table which stores the user login info
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(80))
    favorites = db.relationship('recipe_table', secondary='user_favorites_list', backref='hasFavorited')

    def __repr__(self):
        return f'User(id={self.id}, name={self.name}, email={self.email}, password={self.password})'

user_favorites = db.Table('user_favorites_list',
    db.Column('userID', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('recipeID', db.Integer, db.ForeignKey('recipe_table.id'), primary_key=True)
)

filter_table = db.Table(
    "filter_table",
    # db.Column('recipe_table_id', db.Integer(), db.ForeignKey('recipe_table.id')),
    # db.Column('ingredients_table_id', db.Integer(), db.ForeignKey('ingredients_table.id')),
    db.Column('recipe_table_ingName', db.Integer(), db.ForeignKey('recipe_table.ingName')),
    db.Column('ingredients_table_name', db.Integer(), db.ForeignKey('ingredients_table.name'))
     )

class ingredients_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __repr__(self):
        return f'Ingredient(id={self.id}, name={self.name})'

class recipe_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    calories = db.Column(db.String(100))
    fat = db.Column(db.String(100))
    sugar = db.Column(db.String(100))
    ingName = db.Column(db.String(100))

    def __repr__(self):
        return f'Recipe(id={self.id}, name={self.name}, calories={self.calories}, fat={self.fat}, sugar={self.sugar}, ingName={self.ingName})'
