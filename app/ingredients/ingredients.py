from stat import S_IWUSR
from flask import Blueprint, render_template

ingredients = Blueprint("ingredients", __name__, static_folder="static", template_folder="templates")

ingredientList = [
    {'id': 1, 'name': 'Bananas'},
    {'id': 2, 'name': 'Blueberries'},
    {'id': 3, 'name': 'Cherries'},
    {'id': 4, 'name': 'Kale'},
    {'id': 5, 'name': 'Mangoes'},
    {'id': 6, 'name': 'Oats'},
    {'id': 7, 'name': 'Peaches'},
    {'id': 8, 'name': 'Peanuts'},
    {'id': 9, 'name': 'Strawberries'}
]


@ingredients.route("/ingredients")
@ingredients.route("/")
def index():
    return render_template("Ingredients.html", ingredientList = ingredientList)