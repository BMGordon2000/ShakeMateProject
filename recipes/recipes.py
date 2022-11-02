from flask import Blueprint, render_template
from DatabaseComponent import Recipe
from __init__ import db


recipes = Blueprint("recipes", __name__,
                    static_folder="static", template_folder="templates")


@recipes.route("/recipes")
@recipes.route("/")
def index():
    return render_template("Recipes.html", recipes_list=recipes_list)


@recipes.route("/detailed/<int:recipe_id>")
def recipe_detailed(recipe_id):
    recipe = next(
        (recipe for recipe in recipes if recipe["id"] == recipe_id), None)
    if recipe is None:
        abort(404, description="No recipe was found with the given ID")
    return render_template("detailed.html", recipe=recipe)

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

# for recipe in recipes_list:
#     new_recipe = Recipe(id=recipe.get('id'), shake_name=recipe.get('shake_name'), calories=recipe.get(
#         'calories'), fat=recipe.get('fat'), sugar=recipe.get('sugar'))
#     db.session.add(new_recipe)
# db.session.commit()



