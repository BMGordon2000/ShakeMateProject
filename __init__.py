from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from datetime import timedelta
from flask_migrate import Migrate


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    migrate = Migrate(app, db)
    app.config['SECRET_KEY'] = 'hjdsfsdf'
    # this creates the database as a personal file in called test.db
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///test.db'
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=7)
    db.init_app(app)

    from recipes.recipes import recipes
    from index.index import index
    # these imports are the blueprints
    from ingredients.ingredients import ingredients
    from account.account import account
    from authentication.authentication import authentication
    from favorites.favorites import favorites

    app.register_blueprint(index, url_prefix="")
    app.register_blueprint(recipes, url_prefix="/recipes")
    # these registers the blueprints so they
    app.register_blueprint(ingredients, url_prefix="/ingredients")
    # can be used in the app in differnt files
    app.register_blueprint(account, url_prefix="/account")
    app.register_blueprint(authentication, url_prefix="")
    app.register_blueprint(favorites, url_prefix="")

    from DatabaseComponent import users

    login_manager = LoginManager()
    # controls the login with in the authentication branch
    login_manager.login_view = 'authentication.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # loads the users id which contain the emails, names and passwords.
        return users.query.get(int(id))

    with app.app_context():
        db.create_all()
    return app
