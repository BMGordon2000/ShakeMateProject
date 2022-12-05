import pytest 
from app.DatabaseComponent import User, recipe_table
from app.__init__ import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

def test_favorites():
    """
    appends a recipe to a user's favorite list
    creates own objects
    """
    user1 = User(name='drake', email='drake@gmail.com', password='drake12345')
    recipe1 = recipe_table(name='testRecipe', calories=350, fat=20, sugar=50)
    user1.favorites.append(recipe1)
    assert user1.favorites == [recipe1]

def test_favorites_with_fixture(new_recipe, new_user):
    """
    appends a recipe to a user's favorite list
    uses fixtures for user and recipe objects
    """
    new_user.favorites.append(new_recipe)
    assert new_user.favorites == [new_recipe]

def test_favorited():
    """
    appends a user to a recipes favorites backref and checks if it is there
    creates own objects
    """
    user1 = User(name='drake', email='drake@gmail.com', password='drake12345')
    recipe1 = recipe_table(name='testRecipe', calories=350, fat=20, sugar=50)
    recipe1.hasFavorited.append(user1)
    assert recipe1.hasFavorited == [user1]

def test_favorited_with_fixture(new_recipe, new_user):
    """
    appends a user to a recipes favorites backref and checks if it is there
    uses fixtures for user and recipe objects
    """
    new_recipe.hasFavorited.append(new_user)
    assert new_recipe.hasFavorited[0] == new_user