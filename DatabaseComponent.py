# Database Component
# from Shake import *
# from User import *
# from ingredients.Ingredient import *
from flask_login import UserMixin
from __init__ import db


class users(db.Model, UserMixin):  # creates the database table which stores the user login info
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(80))


recipes_list = [
    {"id": 1, "shake_name": "Brown shake with nuts",
        "calories": 250, "fat": 8, "sugar": 9},
    {"id": 2, "shake_name": "Brown shake", "calories": 235, "fat": 7, "sugar": 7},
    {"id": 3, "shake_name": "Dark green shake",
        "calories": 60, "fat": 1, "sugar": 2},
    {"id": 4, "shake_name": "Dark orange shake",
        "calories": 120, "fat": 4, "sugar": 4},
    {"id": 5, "shake_name": "Dark purple shake",
        "calories": 130, "fat": 7, "sugar": 6},
    {"id": 6, "shake_name": "Dark red shake",
        "calories": 145, "fat": 2, "sugar": 7},
    {"id": 7, "shake_name": "Light green shake",
        "calories": 90, "fat": 1, "sugar": 1},
    {"id": 8, "shake_name": "Light orange shake",
        "calories": 160, "fat": 7, "sugar": 9},
    {"id": 9, "shake_name": "Light purple shake",
        "calories": 140, "fat": 5, "sugar": 4},
    {"id": 10, "shake_name": "Light red shake",
        "calories": 145, "fat": 4, "sugar": 3},
    {"id": 11, "shake_name": "Light yellow shake",
        "calories": 180, "fat": 8, "sugar": 5},
    {"id": 12, "shake_name": "White shake",
        "calories": 220, "fat": 10, "sugar": 12},
]

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shake_name = db.Column(db.String(64))
    calories = db.Column(db.String(20))
    fat = db.Column(db.String(20))
    sugar = db.Column(db.String(20))

    def repr(self):
        return f"Recipe('{self.id}','{self.shake_name}','{self.calories}','{self.fat}','{self.sugar}')"


# recipes = Recipe.query.all()
# for r in recipes:
#     print(r.id, r.shake_name, r.calories, r.fat, r.sugar)


# def IngredientInfo(filter: List[Ingredient]) -> List[Ingredient]:
#     """
#     This method returns each ingredient and its nutrition info
#     :param filter: filters to load only selected ingredients, has no filter if empty list
#     :return: a multivalued list of ingredients and its nutrition information
#     """
#     pass

# def getUserInfo(user: User) -> (email, password):
#     """
#     This method returns the current user's email and password
#     :param: A user object
#     :return: A tuple consisting of email and password
#     """
#     pass

# def getUserHistory(user: User) -> List[Shake]:
#     """
#     This method returns a list of the current user's recently viewed shakes
#     :param user: The current user object
#     :return: A List containing Shake objects
#     """
#     pass

# def getUserFavorites(user: User) -> List[Shake]:
#     """
#     This method returns the current user's entire favorites list
#     :param: A user object
#     :return: A List containing Shake objects
#     """
#     pass
