from stat import S_IWUSR
from flask import Blueprint, render_template,flash,request,redirect,url_for,session
from app.DatabaseComponent import recipe_table, User
from flask_login import current_user

recipes = Blueprint("recipes", __name__,
                    static_folder="static", template_folder="templates")

# recipes_list = [
#     {"id": 1, "name": "Brown shake with nuts",
#         "calories": 250, "fat": 8, "sugar": 9},
#     {"id": 2, "name": "Brown shake", "calories": 235, "fat": 7, "sugar": 7},
#     {"id": 3, "name": "Dark green shake", "calories": 60, "fat": 1, "sugar": 2},
#     {"id": 4, "name": "Dark orange shake", "calories": 120, "fat": 4, "sugar": 4},
#     {"id": 5, "name": "Dark purple shake", "calories": 130, "fat": 7, "sugar": 6},
#     {"id": 6, "name": "Dark red shake", "calories": 145, "fat": 2, "sugar": 7},
#     {"id": 7, "name": "Light green shake", "calories": 90, "fat": 1, "sugar": 1},
#     {"id": 8, "name": "Light orange shake", "calories": 160, "fat": 7, "sugar": 9},
#     {"id": 9, "name": "Light purple shake", "calories": 140, "fat": 5, "sugar": 4},
#     {"id": 10, "name": "Light red shake", "calories": 145, "fat": 4, "sugar": 3},
#     {"id": 11, "name": "Light yellow shake",
#         "calories": 180, "fat": 8, "sugar": 5},
#     {"id": 12, "name": "White shake", "calories": 220, "fat": 10, "sugar": 12},
# ]


@recipes.route("/recipes")
@recipes.route("/", methods=["GET", "POST"])
def index():
    recipes_list = recipe_table.query.order_by(recipe_table.id).all()
    # if request.method == 'POST':
    #     favorite = request.form.get('favorites')

    #     favoriteList = favorites_list.query.filter_by(user_id=current_user.id).first()
        


    return render_template("Recipes.html", recipes_list=recipes_list)


@recipes.route("/detailed/<int:recipe_id>")
def recipe_detailed(recipe_id):
    recipe = next(
        (recipe for recipe in recipes if recipe["id"] == recipe_id), None)
    if recipe is None:
        abort(404, description="No recipe was found with the given ID")
    return render_template("detailed.html", recipe=recipe)