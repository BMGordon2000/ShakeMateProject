from stat import S_IWUSR
from flask import Blueprint, render_template, request, jsonify
from app.DatabaseComponent import ingredients_table, recipe_table

ingredients = Blueprint("ingredients", __name__, static_folder="static", template_folder="templates")

@ingredients.route("/ingredients")
@ingredients.route("/")
def index():
    ingredientList = ingredients_table.query.order_by(ingredients_table.id).all()
    return render_template("Ingredients.html", ingredientList = ingredientList)

@ingredients.route("/getshakes", methods = ["POST"])
def getShakes():
    shakes = []
    data = request.json["items"]
    for i in data:
        shake = recipe_table.query.filter_by(ingName=i).all()
        for j in shake:
            myShake = recipe_table.query.filter_by(ingName=i).first()
            # print(myShake)
            shakes.append(myShake.name)
            # print(j)
            # shakes.append(shake.name) # In the future shake.name would be added to the javascript that would point to the url that would contain the recipe link
        # print(shake)
        # shakes.append(shake.name) # In the future shake.name would be added to the javascript that would point to the url that would contain the recipe link 
    # print(data)
    print(shakes)
    r = jsonify({"value":f"{shakes}"})
    r.status_code = 200
    return r