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
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgres://uxlnsyrkvmscyw:e4d26cbc6d6530745a4a5af15df2cf91965d23aff7a4b48596b309d6db422ac3@ec2-52-20-166-21.compute-1.amazonaws.com:5432/d3idthv2dsdhhr') or \
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

    app.register_blueprint(index.index, url_prefix="")
    app.register_blueprint(recipes.recipes, url_prefix="/recipes")
    # these registers the blueprints so they
    app.register_blueprint(ingredients.ingredients, url_prefix="/ingredients")
    # can be used in the app in differnt files
    app.register_blueprint(account.account, url_prefix="")
    app.register_blueprint(authentication.authentication, url_prefix="")

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
                # u = User(name="Bob", email="bob@abc.com", password="abc123")
                # db.session.add(u)
                # db.session.commit()
                print("The user is added. Inspect the database file or re-run the app to see it.")

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
                        "calories": 5000, "fat": 0, "sugar": 0, "recipetext": "The greatest shake of all time, it is infinitely powerful"},
                    {"id": 2, "name": "Banana Shake",
                        "calories": 235, "fat": 7, "sugar": 7, "recipetext": "Combine 1 banana and 1/4 cup milk in a blender and blend until smooth."},
                    {"id": 3, "name": "Strawberry Banana Shake",
                        "calories": 60, "fat": 1, "sugar": 2, "recipetext": "Pour 1/2 cup milk in a blender. Add 1/4 cup halved strawberries. Add 1/2 of a banana. Add 1/2 tbsp sugar."},
                    {"id": 4, "name": "Cherry-Blueberry Banana Shake",
                        "calories": 120, "fat": 4, "sugar": 4, "recipetext": "In a blender combine 1/2 cup cherries WITHOUT SEEDS, 1 cup yogurt, 1/4 cup blueberries, and 1/4 cup sliced banana. Cover and blend until smooth."},
                    {"id": 5, "name": "Orange Vanilla Shake",
                        "calories": 130, "fat": 7, "sugar": 6, "recipetext": "Cut 1 orange into halves and remove seeds and peel and dice into large pieces. Add into blender with 1 tsp vanilla and 1 cup milk and blend until smooth."},
                    {"id": 6, "name": "Triple Berry Oat Shake",
                        "calories": 145, "fat": 2, "sugar": 7, "recipetext": "Add 1/4 cup frozen blueberries, 1/4 cup frozen raspberries, 1/2 cup frozen strawberries, 1/2 cup rolled oats, 1/2 cup yogurt, and 1 banana to the blender and blend until smooth."},
                    {"id": 7, "name": "Tropical Coconut Shake",
                        "calories": 90, "fat": 1, "sugar": 1, "recipetext": "Place 1/2 cup frozen pineapple, 1/2 cup yogurt, 1/4 cup shaved coconut, and 1/4 cup milk in blender and blend until smooth."},
                    {"id": 8, "name": "Healthy Kale Smoothie",
                        "calories": 160, "fat": 7, "sugar": 9, "recipetext": "Place all ingredients (2 cups kale, 3/4 cup milk, 1 banana, 1/4 cup yogurt, 1/4 cup pineapple, 2 tbsp peanut butter, and 1 tsp sugar) in a blender and blend until smooth"},
                    {"id": 9, "name": "Strawberry Smoothie",
                        "calories": 140, "fat": 5, "sugar": 4, "recipetext": "Combine 1 cup strawberries, 1 cup yogurt, 1 tsp vanilla, 1/8 cup oats, and 1 tsp sugar into blender and blend until smooth"},
                    {"id": 10, "name": "Peanut Butter Banana Shake",
                        "calories": 145, "fat": 4, "sugar": 3, "recipetext": "Combine 1 banana, 1 cup yogurt, 1/4 cup peanut butter, 1 tsp cinnamon, and 1 tsp sugar into blender and blend until smooth"},
                    {"id": 11, "name": "Strawberry Mango Shake",
                        "calories": 180, "fat": 8, "sugar": 5, "recipetext": "Combine 1/2 cup strawberries, 1 cup yogurt, 1/2 cup mango chunks, and 1 tsp sugar into blender and blend until smooth"},
                    {"id": 12, "name": "Peach Smoothie",
                        "calories": 220, "fat": 7, "sugar": 12, "recipetext": "Combine 1 cup frozen peaches, 1 cup yogurt, 1/2 cup milk, 1 tsp vanilla, and 1 tsp sugar into blender and blend until smooth"},
                    {"id": 13, "name": "Tropical Smoothie",
                        "calories": 110, "fat": 5, "sugar": 5, "recipetext": "Combine 1/2 banana, 1 cup yogurt, 1/4 cup mango chunks, 1/4 cup peeled orange, 1/4 cup frozen pineapple, and 1 tsp sugar into blender and blend until smooth"},    
                    {"id": 14, "name": "Sunrise Shake",
                        "calories": 50, "fat": 2, "sugar": 3, "recipetext": "Combine 1/4 cup strawberries, 1 cup yogurt, 1/4 cup mango chunks, 1/4 cup juiced orange, 1/4 cup frozen pineapple, and 1 tsp maple syrup into blender and blend until smooth"},
                    {"id": 15, "name": "Creamy Peanut Butter Shake",
                        "calories": 140, "fat": 9, "sugar": 20, "recipetext": "Add 1 cup milk, 1/2 cup vanilla ice cream, and 1 cup peanut butter into the blender and blend until smooth"},
                    {"id": 16, "name": "Kale Smoothie",
                        "calories": 120, "fat": 10, "sugar": 5, "recipetext": "Combine 1/2 cup kale, 1 cup milk, 1/4 cup peach chunks, 1/4 cup sliced banana, and 1 tsp maple syrup into blender and blend until smooth"},
                    {"id": 17, "name": "Strawberry Kiwi Shake",
                        "calories": 213, "fat": 2, "sugar": 22, "recipetext": "Add 1 kiwi, 1/2 cup strawberries, 1 tbsp of yogurt, and 1 cup of milk into a blender and blend until smooth"}
                ]
                for i in range(len(recipes_list)):
                    new_recipe = recipe_table(id=recipes_list[i].get("id"), name=recipes_list[i].get("name"), calories=recipes_list[i].get("calories"),
                                              fat=recipes_list[i].get("fat"), sugar=recipes_list[i].get("sugar"), recipetext=recipes_list[i].get("recipetext"))
                    db.session.add(new_recipe)
                    db.session.commit()
                print("The recipes are added. Inspect the database file or re-run the app to see it.")
        
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
                    {'id': 9, 'name': 'Strawberries'},
                    {'id': 10, 'name': 'Oranges'},
                    {'id': 11, 'name': 'Vanilla'},
                    {'id': 12, 'name': 'Coconut'},
                    {'id': 13, 'name': 'Pineapple'},
                    {'id': 14, 'name': 'Raspberries'},
                    {'id': 15, 'name': 'Kiwis'}
                ]
                for i in range(len(ingredientList)):
                    new_ingredient = ingredients_table(id=ingredientList[i].get("id"), name=ingredientList[i].get("name"))
                    db.session.add(new_ingredient)
                    db.session.commit()
                print("The ingredients are added. Inspect the database file or re-run the app to see it.")

        if not inspector.has_table('filter_table'):
            print("Filter table does not exist! did you run 'flask db upgrade' from the terminal?")
        else:
            print("Filter table already exists!")
            current_ingredients = ingredients_table.query.all()
            current_recipe = recipe_table.query.all()
            # brown shake with nuts
            current_recipe[0].ingredients.append(current_ingredients[7])
            # Banana shake
            current_recipe[1].ingredients.append(current_ingredients[0])
            # Strawberry Banana Shake
            current_recipe[2].ingredients.append(current_ingredients[0])
            current_recipe[2].ingredients.append(current_ingredients[8])
            # Cherry-Blueberry Banana Shake
            current_recipe[3].ingredients.append(current_ingredients[0])
            current_recipe[3].ingredients.append(current_ingredients[1])
            current_recipe[3].ingredients.append(current_ingredients[2])
            # Orange Vanilla Shake
            current_recipe[4].ingredients.append(current_ingredients[9])
            current_recipe[4].ingredients.append(current_ingredients[10])
            # Triple Berry Oat Shake
            current_recipe[5].ingredients.append(current_ingredients[0])
            current_recipe[5].ingredients.append(current_ingredients[1])
            current_recipe[5].ingredients.append(current_ingredients[13])
            current_recipe[5].ingredients.append(current_ingredients[8])
            current_recipe[5].ingredients.append(current_ingredients[5])
            # Tropical Shake
            current_recipe[6].ingredients.append(current_ingredients[11])
            current_recipe[6].ingredients.append(current_ingredients[12])
            # Healthy Kale Shake
            current_recipe[7].ingredients.append(current_ingredients[0])
            current_recipe[7].ingredients.append(current_ingredients[12])
            current_recipe[7].ingredients.append(current_ingredients[3])
            # Strawberry Smoothie
            current_recipe[8].ingredients.append(current_ingredients[8])
            current_recipe[8].ingredients.append(current_ingredients[5])
            current_recipe[8].ingredients.append(current_ingredients[10])
            # Peanut Butter Banana Shake
            current_recipe[9].ingredients.append(current_ingredients[0])
            current_recipe[9].ingredients.append(current_ingredients[7])
            # Strawberry Mango Shake
            current_recipe[10].ingredients.append(current_ingredients[8])
            current_recipe[10].ingredients.append(current_ingredients[4])
        	# Peach Smoothie
            current_recipe[11].ingredients.append(current_ingredients[6])
            current_recipe[11].ingredients.append(current_ingredients[10])
            # Tropical Smoothie
            current_recipe[12].ingredients.append(current_ingredients[0])
            current_recipe[12].ingredients.append(current_ingredients[4])
            current_recipe[12].ingredients.append(current_ingredients[12])
            current_recipe[12].ingredients.append(current_ingredients[9])
            # Sunrise Shake
            current_recipe[13].ingredients.append(current_ingredients[8])
            current_recipe[13].ingredients.append(current_ingredients[4])
            current_recipe[13].ingredients.append(current_ingredients[12])
            current_recipe[13].ingredients.append(current_ingredients[9])
            # Creamy Peanut Butter Shake
            current_recipe[14].ingredients.append(current_ingredients[7])
            # Kale Smoothie
            current_recipe[15].ingredients.append(current_ingredients[0])
            current_recipe[15].ingredients.append(current_ingredients[3])
            current_recipe[15].ingredients.append(current_ingredients[6])
            # Strawberry Kiwi Shake
            current_recipe[16].ingredients.append(current_ingredients[14])
            current_recipe[16].ingredients.append(current_ingredients[8])
            db.session.commit()
                
            # Setting ingredients to the recipes they are in for the filter    
    with app.app_context():
        db.create_all()

    return app
