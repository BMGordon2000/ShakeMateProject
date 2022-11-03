from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from flask_login import LoginManager
from flask_migrate import Migrate
from datetime import timedelta

import os

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjdsfsdf'
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + \
        os.path.join(
            'test.db')  # this creates the database as a personal file in called test.db
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=7)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.recipes import recipes
    from app.index import index
    from app.ingredients import ingredients  # these imports are the blueprints
    from app.account import account
    from app.authentication import authentication
    from app.favorites import favorites

    app.register_blueprint(index.index, url_prefix="")
    app.register_blueprint(recipes.recipes, url_prefix="/recipes")
    # these registers the blueprints so they
    app.register_blueprint(ingredients.ingredients, url_prefix="/ingredients")
    # can be used in the app in differnt files
    app.register_blueprint(account.account, url_prefix="/account")
    app.register_blueprint(authentication.authentication, url_prefix="")
    app.register_blueprint(favorites.favorites, url_prefix="")

    from app import DatabaseComponent

    login_manager = LoginManager()
    # controls the login with in the authentication branch
    login_manager.login_view = 'authentication.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        # loads the users id which contain the emails, names and passwords.
        return DatabaseComponent.User.query.get(int(id))

    from app.DatabaseComponent import User
    from app.DatabaseComponent import ingredients_table
    from app.DatabaseComponent import recipe_table

    with app.app_context():
        # You create the database and tables by following the instructions in the README.md
        # You populate the tables with data by writing some code here.

        inspector = inspect(db.engine)

        # First, make sure the table you are trying to populate exists.
        # Make sure the table exists before doing anything with it
        if not inspector.has_table('user'):
            print(
                "user table does not exist! did you run 'flask db upgrade' from the terminal?")
        else:
            current_users = User.query.all()
            # First, check to see if there is already data. If so, do not add your initial data.
            if current_users:
                print("The user table already exists! Printing all users...")
                for u in current_users:
                    print(f'\t{u}')
                print("I printed them!")
            else:
                print("No users detected. Adding one!")
                u = User(name="Bob", email="bob@abc.com", password="abc123")
                db.session.add(u)
                db.session.commit()
                print(
                    "The user is added. Inspect the database file or re-run the app to see it.")

        # Make sure the table exists before doing anything with it
        if not inspector.has_table('recipe_table'):
            print(
                "Recipe table does not exist! Did you run 'flask db upgrade' from the terminal?")
        else:
            current_recipe = recipe_table.query.all()
            # First, check to see if there is already data. If so, do not add your initial data.
            if current_recipe:
                print("The recipe table already exists! Printing all recipes...")
                for i in current_recipe:
                    print(f'\t{i}')
                print("I printed them!")
            else:
                print("No recipes detected. Adding them")
                recipes_list = [
                    {"id": 1, "name": "Brown shake with nuts",
                        "calories": 250, "fat": 8, "sugar": 9},
                    {"id": 2, "name": "Brown shake",
                        "calories": 235, "fat": 7, "sugar": 7},
                    {"id": 3, "name": "Dark green shake",
                        "calories": 60, "fat": 1, "sugar": 2},
                    {"id": 4, "name": "Dark orange shake",
                        "calories": 120, "fat": 4, "sugar": 4},
                    {"id": 5, "name": "Dark purple shake",
                        "calories": 130, "fat": 7, "sugar": 6},
                    {"id": 6, "name": "Dark red shake",
                        "calories": 145, "fat": 2, "sugar": 7},
                    {"id": 7, "name": "Light green shake",
                        "calories": 90, "fat": 1, "sugar": 1},
                    {"id": 8, "name": "Light orange shake",
                        "calories": 160, "fat": 7, "sugar": 9},
                    {"id": 9, "name": "Light purple shake",
                        "calories": 140, "fat": 5, "sugar": 4},
                    {"id": 10, "name": "Light red shake",
                        "calories": 145, "fat": 4, "sugar": 3},
                    {"id": 11, "name": "Light yellow shake",
                        "calories": 180, "fat": 8, "sugar": 5},
                    {"id": 12, "name": "White shake",
                        "calories": 220, "fat": 10, "sugar": 12},
                ]
                for i in range(len(recipes_list)):
                    new_recipe = recipe_table(name=recipes_list[i].get("name"), calories=calories_list[i].get("calories"),
                                              fat=recipes_list[i].get("fat"), sugar=recipes_list[i].get("sugar"))
                    db.session.add(new_recipe)
                db.session.commit()

    #
    # with app.app_context():
    #     db.create_all()

    return app
