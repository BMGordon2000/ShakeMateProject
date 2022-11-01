from stat import S_IWUSR
from flask import Blueprint, render_template
from DatabaseComponent import ingredients
from __init__ import db

ingredients = Blueprint("ingredients", __name__, static_folder="static", template_folder="templates")

# Fat and sugar values are in grams and smaller ingredients show data for 1 cup
ingredientList = [
    {'id': 1, 'name': 'Bananas', 'caloricData': 110, 'fat': 0, 'sugar': 15},
    {'id': 2, 'name': 'Blueberries', 'caloricData': 84, 'fat': 0.5, 'sugar': 21},
    {'id': 3, 'name': 'Cherries', 'caloricData': 87, 'fat': 0.3, 'sugar': 22},
    {'id': 4, 'name': 'Kale', 'caloricData': 7.4, 'fat': 0.3, 'sugar': 0.2},
    {'id': 5, 'name': 'Mangoes', 'caloricData': 202, 'fat': 0, 'sugar': 46},
    {'id': 6, 'name': 'Oats', 'caloricData': 307, 'fat': 5.3, 'sugar': 0.8},
    {'id': 7, 'name': 'Peaches', 'caloricData': 50, 'fat': 0.5, 'sugar': 13},
    {'id': 8, 'name': 'Peanuts', 'caloricData': 828, 'fat': 71.9, 'sugar': 5.8},
    {'id': 9, 'name': 'Strawberries', 'caloricData': 49, 'fat': 0.5, 'sugar': 7.4}
]


@ingredients.route("/ingredients")
@ingredients.route("/")
def index():
    return render_template("Ingredients.html", ingredientList = ingredientList)