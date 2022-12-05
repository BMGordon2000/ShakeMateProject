from flask import Blueprint, render_template

favorites = Blueprint("favorites", __name__, static_folder="static", template_folder="templates")

@favorites.route("/favorites")
def index():
    return render_template("Favorites_History.html")