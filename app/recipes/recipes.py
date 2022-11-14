from stat import S_IWUSR
from flask import Blueprint, render_template,flash,request,redirect,url_for,session, request
from app.DatabaseComponent import recipe_table, User
from flask_login import current_user, ingredients_table, db

recipes = Blueprint("recipes", __name__,
                    static_folder="static", template_folder="templates")


@recipes.route("/recipes")
@recipes.route("/", methods=["GET", "POST"])
def index():
    recipes_list = recipe_table.query.order_by(recipe_table.id).all()
    # if request.method == 'POST':
    #     favorite = request.form.get('favorites')

    #     favoriteList = favorites_list.query.filter_by(user_id=current_user.id).first()
        


    return render_template("Recipes.html", recipes_list=recipes_list)


@recipes.route("/filteredRecipes")
@recipes.route("/")
def filtercomponet():

    
    filters= recipe_table.ingName == 'Bananas',ingredients_table.name == 'Bananas'
    filterd = recipe_table.query.filter(*filters).all()

    return render_template("filteredRecipes.html", filterd=filterd)

@recipes.route("/detailed/<int:recipe_id>")
def recipe_detailed(recipe_id):
    recipe = next(
        (recipe for recipe in recipes if recipe["id"] == recipe_id), None)
    if recipe is None:
        abort(404, description="No recipe was found with the given ID")
    return render_template("detailed.html", recipe=recipe)