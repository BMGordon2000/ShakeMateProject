from flask import Blueprint, render_template

ingredients = Blueprint("ingredients", __name__, static_folder="static", template_folder="templates")

@ingredients.route("/ingredients")
@ingredients.route("/")
def index():
    return render_template("Ingredients.html")