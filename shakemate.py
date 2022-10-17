from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy




webapp = Flask(__name__)
webapp.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
webapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(webapp)


class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(80))

    
    with webapp.app_context():
        db.create_all()

@webapp.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html')

@webapp.route('/ingredients', methods=["GET", "POST"])
def ingredients():
    return render_template('Ingredients.html')

@webapp.route('/recipes', methods=["GET", "POST"])
def recipes():
    return render_template('Recipes.html')

@webapp.route('/account', methods=["GET", "POST"])
def account():
    return render_template('Account.html')

@webapp.route('/authenticate', methods=["GET", "POST"])
def authenticate():
    return render_template('Authentication.html')

@webapp.route('/Fav_Hist', methods=["GET", "POST"])
def fav_hist():
    return render_template('Favorites_History.html')

@webapp.route('/signup', methods=["GET", "POST"])
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    webapp.run(debug=True)
