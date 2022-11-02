from nis import cat
from flask import Blueprint, render_template,flash,request,redirect,url_for,session
from DatabaseComponent import users
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db
from flask_login import login_user, current_user, logout_user

authentication = Blueprint("authentication", __name__,
                           static_folder="static", template_folder="templates")


@authentication.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password1')

        user = users.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in was successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('account.Account'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist or was typed in wrong.', category='error')

    return render_template("Authentication.html", user=current_user)    


@authentication.route('/signup', methods=['GET', 'POST'])
def signup(): 
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = users.query.filter_by(email=email).first()
        if user:
            flash('Email has already been created.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = users(email=email, name=name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account has been created!', category='success')
            return redirect(url_for('authentication.login'))

    return render_template("signup.html", user=current_user)

@authentication.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('authentication.login'))