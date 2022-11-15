from stat import S_IWUSR
from flask import Blueprint, render_template,flash,request,redirect,url_for,session, request
from app.DatabaseComponent import recipe_table, User, ingredients_table, user_favorites_list
from app import db
from flask_login import current_user

recipes = Blueprint("recipes", __name__,
                    static_folder="static", template_folder="templates")


@recipes.route("/recipes", methods=['GET', 'POST'])
@recipes.route("/", methods=['GET', 'POST'])
def index():
    recipes_list = recipe_table.query.order_by(recipe_table.id).all()
    favoriteList = current_user.favorites

    if request.method == 'POST':
        recipe_id = request.form['recipe']
        recipeToChange = recipes_list[int(recipe_id) - 1]
        if recipeToChange not in favoriteList:
            current_user.favorites.append(recipeToChange)
            db.session.commit()
            flashMessage = recipeToChange.name + ' added to favorites!'
            flash(flashMessage, category='success')
            return render_template("Recipes.html", recipes_list=recipes_list, favoriteList=favoriteList)
        else:
            current_user.favorites.remove(recipeToChange)
            db.session.commit()
            flashMessage = recipeToChange.name + 'removed from favorites!'
            flash(flashMessage, category='success')
            return render_template("Recipes.html", recipes_list=recipes_list, favoriteList=favoriteList)
    else:
        return render_template("Recipes.html", recipes_list=recipes_list, favoriteList=favoriteList)


@recipes.route("/filteredRecipes", methods=['GET', 'POST'])
@recipes.route("/", methods=['GET', 'POST'])
def filtercomponet():

    
    filters= recipe_table.ingName == 'Bananas',ingredients_table.name == 'Bananas'
    filterd = recipe_table.query.filter(*filters).all()

    return render_template("filteredRecipes.html", filterd=filterd)

@recipes.route("/detailed/<int:recipe_id>", methods=['GET', 'POST'])
def recipe_detailed(recipe_id):
    recipe = next(
        (recipe for recipe in recipes if recipe["id"] == recipe_id), None)
    if recipe is None:
        abort(404, description="No recipe was found with the given ID")
    return render_template("detailed.html", recipe=recipe)