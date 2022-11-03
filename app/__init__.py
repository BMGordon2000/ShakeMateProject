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
        'sqlite:///' + os.path.join('test.db') #this creates the database as a personal file in called test.db
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=7)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.recipes import recipes
    from app.index import index
    from app.ingredients import ingredients #### these imports are the blueprints
    from app.account import account
    from app.authentication import authentication
    from app.favorites import favorites

    app.register_blueprint(index.index, url_prefix="")
    app.register_blueprint(recipes.recipes, url_prefix="/recipes")
    app.register_blueprint(ingredients.ingredients, url_prefix="/ingredients") ### these registers the blueprints so they
    app.register_blueprint(account.account, url_prefix="/account")     ### can be used in the app in differnt files
    app.register_blueprint(authentication.authentication, url_prefix="")
    app.register_blueprint(favorites.favorites, url_prefix="")

    from app import DatabaseComponent

    login_manager = LoginManager() 
    login_manager.login_view = 'authentication.login' # controls the login with in the authentication branch
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return DatabaseComponent.User.query.get(int(id)) #loads the users id which contain the emails, names and passwords.


    from app.DatabaseComponent import User
    from app.DatabaseComponent import ingredients_table

    with app.app_context():
        # You create the database and tables by following the instructions in the README.md
        # You populate the tables with data by writing some code here.

        inspector = inspect(db.engine)

        # First, make sure the table you are trying to populate exists.
        if not inspector.has_table('user'):    # Make sure the table exists before doing anything with it
            print("user table does not exist! did you run 'flask db upgrade' from the terminal?")
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
                print("The user is added. Inspect the database file or re-run the app to see it.")
        

        if not inspector.has_table('ingredients_table'):    # Make sure the table exists before doing anything with it
            print("Ingredient table does not exist! did you run 'flask db upgrade' from the terminal?")
        else:
            current_ingredients = ingredients_table.query.all()
            # First, check to see if there is already data. If so, do not add your initial data.
            if current_ingredients:
                print("The ingredient table already exists! Printing all ingredients...")
                for i in current_ingredients:
                    print(f'\t{i}')
                print("I printed them!")
            else:
                print("No ingredients detected. Adding them")
                ingredientList = [
                    {'id': 1, 'name': 'Bananas'},
                    {'id': 2, 'name': 'Blueberries'},
                    {'id': 3, 'name': 'Cherries'},
                    {'id': 4, 'name': 'Kale'},
                    {'id': 5, 'name': 'Mangoes'},
                    {'id': 6, 'name': 'Oats'},
                    {'id': 7, 'name': 'Peaches'},
                    {'id': 8, 'name': 'Peanuts'},
                    {'id': 9, 'name': 'Strawberries'}
                ]
                for i in range(len(ingredientList)):
                    new_ingredient = ingredients_table(name=ingredientList[i].get("name"))
                    db.session.add(new_ingredient)
                db.session.commit()


    #
    # with app.app_context():
    #     db.create_all()

    return app


