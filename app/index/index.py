from flask import Blueprint, render_template

index = Blueprint("index", __name__, static_folder="static", template_folder="templates")

@index.route("/")
def home_index():
    # return render_template("index.html")
    return render_template("Authentication.html")