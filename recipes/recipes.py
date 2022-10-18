from flask import Blueprint, render_template


recipes = Blueprint("recipes", __name__, static_folder="static", template_folder="templates")

recipes_list = [
    {"id": 1, "name": "Brown shake with nuts", "calories": 250, "fat": 8, "sugar": 9 },
    {"id": 1, "name": "Brown shake", "calories": 235, "fat": 7, "sugar": 7 },
    {"id": 1, "name": "Dark green shake", "calories": 60, "fat": 1, "sugar": 2 },
    {"id": 1, "name": "Dark orange shake", "calories": 120, "fat": 4, "sugar": 4 },
    {"id": 1, "name": "Dark purple shake", "calories": 130, "fat": 7, "sugar": 6 },
    {"id": 1, "name": "Dark red shake", "calories": 145, "fat": 2, "sugar": 7 },
    {"id": 1, "name": "Light green shake", "calories": 90, "fat": 1, "sugar": 1 },
    {"id": 1, "name": "Light orange shake", "calories": 160, "fat": 7, "sugar": 9 },
    {"id": 1, "name": "Light purple shake", "calories": 140, "fat": 5, "sugar": 4 },
    {"id": 1, "name": "Light red shake", "calories": 145, "fat": 4, "sugar": 3 },
    {"id": 1, "name": "Light yellow shake", "calories": 180, "fat": 8, "sugar": 5 },
    {"id": 1, "name": "White shake", "calories": 220, "fat": 10, "sugar": 12 },
    ]
@recipes.route("/recipes")
@recipes.route("/")
def index():
    return render_template("Recipes.html", recipes_list = recipes_list)

