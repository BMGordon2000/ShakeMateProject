from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjdsfsdf'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///test.db' #this creates the database as a personal file in called test.db
    db.init_app(app)

    from recipes.recipes import recipes
    from index.index import index
    from ingredients.ingredients import ingredients #### these imports are the blueprints 
    from account.account import account
    from authentication.authentication import authentication
    from favorites.favorites import favorites

    app.register_blueprint(index, url_prefix="")
    app.register_blueprint(recipes, url_prefix="")
    app.register_blueprint(ingredients, url_prefix="") ### these registers the blueprints so they
    app.register_blueprint(account, url_prefix="")     ### can be used in the app in differnt files
    app.register_blueprint(authentication, url_prefix="")
    app.register_blueprint(favorites, url_prefix="")

    from DatabaseComponent import users

    login_manager = LoginManager() 
    login_manager.login_view = 'authentication.login' # controls the login with in the authentication branch
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return users.query.get(int(id)) #loads the users id which contain the emails, names and passwords.


    with app.app_context():
        db.create_all()
    return app


