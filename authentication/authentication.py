from flask import Blueprint, render_template,flash,request,redirect,url_for
from DatabaseComponent import users
from werkzeug.security import generate_password_hash

authentication = Blueprint("authentication", __name__,
                           static_folder="static", template_folder="templates")


@authentication.route("/authenticate")
@authentication.route("/", methods=['GET','POST'])
def index():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        login = users.query.filter_by(username=username, password=password).first()
        if login is not None:
            return redirect(url_for("account.account"))
        else:
            flash("don't know you", category='error')
    return render_template("Authentication.html")



@authentication.route('/signup', methods=['GET', 'POST'])
def signup(): 
    if request.method=='GET': 
        return render_template('signup.html')
    else: 
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        user = users.query.filter_by(email=email).first() 
        if user: 
            flash('Email address already exists')
            return redirect(url_for('authentication.signup'))

        new_user = users(email=email, name=name, password=generate_password_hash(password, method='sha256')) #

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('Authentication.authenticate'))