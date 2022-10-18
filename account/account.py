from flask import Blueprint, render_template

account = Blueprint("account", __name__, static_folder="static", template_folder="templates")

@account.route("/account")
@account.route("/")
def index():
    return render_template("Account.html")