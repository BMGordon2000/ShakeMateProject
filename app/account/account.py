from flask import Blueprint, render_template,flash,request,request
from app.DatabaseComponent import recipe_table
from app import db
from flask_login import current_user, login_required
account = Blueprint("account", __name__,
                    static_folder="static", template_folder="templates")


@account.route("/favoritesList", methods=['GET', 'POST'])
@account.route("/", methods=['GET', 'POST'])
@login_required
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
            return render_template("Account.html", recipes_list=recipes_list, favoriteList=favoriteList)
        else:
            current_user.favorites.remove(recipeToChange)
            db.session.commit()
            flashMessage = recipeToChange.name + ' removed from favorites!'
            flash(flashMessage, category='success')
            return render_template("Account.html", recipes_list=recipes_list, favoriteList=favoriteList)
    else:
        return render_template("Account.html", recipes_list=recipes_list, favoriteList=favoriteList)
