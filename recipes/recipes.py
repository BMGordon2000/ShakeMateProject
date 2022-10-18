from flask import Blueprint, render_template

recipes = Blueprint("recipes", __name__, static_folder="static", template_folder="templates")

@recipes.route("/recipes")
@recipes.route("/")
def index():
    return render_template("Recipes.html")