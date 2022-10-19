# Authentication Component
from flask import Flask ,Blueprint,render_template,flash,request,redirect,url_for
from DatabaseComponent import db
from Shake import Shake
from User import User


authComponent = Blueprint('authComponent', __name__)

@authComponent.route("/authenticate",methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        login = users.query.filter_by(username=username, password=password).first()
        if login is not None:
            return redirect(url_for("account"))
        else:
            flash("don't know you", category='error')
    return render_template("Authentication.html")

@authComponent.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        register = users(username = username, email = email, password = password)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("authenticate"))
    return render_template("signup.html")






# def get_user_data(user: User) -> List[Data]:
#     """
#     This method returns the favorite list for a particular user. Returns an empty list if the favorite list is empty.
#     :param user: the User object for whom you want to get the favorite list
#     :return: a List of recipe objects or an empty list if the user has no favorites
#     """
#     pass
# def Userfavorites(user: User) -> List[Shake]:
#     """
#     This method will line up the particular shake to the user, and return it to the favorites list.
#     :param user: the shake list is sent to the use once favorited
#     :return: a list of shakes or an empty list if the user has no favorites
#     """
#     pass