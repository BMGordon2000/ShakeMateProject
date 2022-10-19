from flask import Blueprint, render_template

account = Blueprint("account", __name__, static_folder="static", template_folder="templates")

@account.route("/account")
def Account():
    return render_template("Account.html")