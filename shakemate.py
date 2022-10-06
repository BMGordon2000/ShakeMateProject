from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

webapp = Flask(__name__)


@webapp.route('/')
def index():
    return render_template('index.html')

@webapp.route('/ingredients')
def ingredients():
    return render_template('Ingredients.html')

@webapp.route('/recipes')
def recipes():
    return render_template('Recipes.html')

@webapp.route('/account')
def account():
    return render_template('Account.html')

@webapp.route('/authenticate')
def authenticate():
    return render_template('Authentication.html')

@webapp.route('/Fav_Hist')
def fav_hist():
    return render_template('Favorites_History.html')
    
if __name__ == "__main__":
    webapp.run(debug=True)
