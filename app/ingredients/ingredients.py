from stat import S_IWUSR
from flask import Blueprint, render_template
from app.DatabaseComponent import ingredients_table
from flask_login import current_user, login_required
ingredients = Blueprint("ingredients", __name__, static_folder="static", template_folder="templates")

@ingredients.route("/ingredients", methods=['GET', 'POST'])
@ingredients.route("/", methods=['GET', 'POST'])
@login_required
def index():
    ingredients_list = ingredients_table.query.order_by(ingredients_table.id).all()
    return render_template("Ingredients.html", ingredients_list=ingredients_list)