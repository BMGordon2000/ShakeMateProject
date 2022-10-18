from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from recipes.recipes import recipes
from index.index import index
from ingredients.ingredients import ingredients
from account.account import account
from authentication.authentication import authentication
from favorites.favorites import favorites

app = Flask(__name__)
app.register_blueprint(index, url_prefix="")
app.register_blueprint(recipes, url_prefix="/recipes")
app.register_blueprint(ingredients, url_prefix="/ingredients")
app.register_blueprint(account, url_prefix="/account")
app.register_blueprint(authentication, url_prefix="/authenticate")
app.register_blueprint(favorites, url_prefix="/Fav_Hist")


if __name__ == "__main__":
    app.run(debug=True)
