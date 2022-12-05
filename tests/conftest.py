import pytest

from app.DatabaseComponent import User, db, recipe_table, ingredients_table
from app.__init__ import create_app
from main import app

# --------
# Fixtures
# --------

@pytest.fixture(scope='module')
def new_user():
    user = User('drake','drake@gmail.com', 'drake12345')
    return user

@pytest.fixture(scope="module")
def new_recipe():
    recipe = recipe_table(id=0, name='testRecipe', calories=350, fat=20, sugar=50, recipetext="recipe text placeholder")
    return recipe

@pytest.fixture(scope='module')
def existing_user():
    user = User('Brian','drake@gmail.com', 'Brian12345')
    return user

@pytest.fixture(scope='module')
def test_recipe_image():
    test_recipe1 = recipe_table(id=23)
    return test_recipe1

@pytest.fixture(scope='module')
def test_client():
    # Create a Flask app configured for testing
    flask_app = create_app()
    flask_app.config.from_object('config.TestingConfig')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    db.create_all()

    # Initialize user data
    user1 = User(name='drake', email='drake@gmail.com', password_plaintext='drake12345')
    user2 = User(email='trafton@gmail.com', password_plaintext='hopefullyThisWorks')

    # Initialize recipe data
    recipe1 = recipe_table(id=0, name='testRecipe', calories=350, fat=20, sugar=50, recipetext="recipe text placeholder")

    # Insert data to db
    db.session.add(user1)
    db.session.add(user2)
    db.session.add(recipe1)

    # Commit the changes
    db.session.commit()

    # Add recipe 1 to user 1's favorite list
    user1.favorites.append(recipe1)

    # Commit the changes
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()


@pytest.fixture(scope='function')
def login_default_user(test_client):
    test_client.post('/login',
                     data=dict(email='drake@gmail.com', password='drake12345'),
                     follow_redirects=True)

    yield  # this is where the testing happens!

    test_client.get('/logout', follow_redirects=True)


@pytest.fixture(scope='module')
def cli_test_client():
    flask_app = create_app()
    flask_app.config.from_object('config.TestingConfig')

    runner = flask_app.test_cli_runner()

    yield runner  # this is where the testing happens!

@pytest.fixture(scope='module')
def new_ingredient_test():
    ing = ingredients_table(id=0, name="PotatoTest")
    return ing