from stat import S_IWUSR
from flask import Blueprint, render_template, request, jsonify
from app.DatabaseComponent import ingredients_table, recipe_table

ingredients = Blueprint("ingredients", __name__, static_folder="static", template_folder="templates")

@ingredients.route("/ingredients", methods=['GET', 'POST'])
@ingredients.route("/", methods=['GET', 'POST'])
def index():
    ingredientList = ingredients_table.query.order_by(ingredients_table.id).all()
    return render_template("Ingredients.html", ingredientList = ingredientList)

@ingredients.route("/getshakes", methods = ['GET', 'POST'])
def getShakes():
    recipes_list = recipe_table.query.order_by(recipe_table.name).all()
    data = request.json["items"]
    ingredient_list = []
    for i in data:
        ingredient_list.append[i]
        
    print(shakes)
    r = jsonify({"value":f"{shakes}"})
    r.status_code = 200
    return r