from flask import Blueprint, render_template

authentication = Blueprint("authentication", __name__,
                           static_folder="static", template_folder="templates")


@authentication.route("/authenticate")
@authentication.route("/")
def index():
    return render_template("Authentication.html")
