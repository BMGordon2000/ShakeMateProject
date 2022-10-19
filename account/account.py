from flask import Blueprint, render_template
from flask_login import login_required
account = Blueprint("account", __name__,
                    static_folder="static", template_folder="templates")


@account.route("/account")
@account.route("/")
@login_required
def Account():
    return render_template("Account.html")
