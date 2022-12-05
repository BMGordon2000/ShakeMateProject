import pytest
from app.DatabaseComponent import User, recipe_table
from app.__init__ import create_app


@pytest.fixture
def app():
    app = create_app()
    return app


def test_new_recipe():
    """
    checks if a recipe is initialized correctly 
    """
    recipe = recipe_table(name='testRecipe', calories=350, fat=20, sugar=50, id=2, recipetext='yum')
    assert recipe.name == 'testRecipe'
    assert recipe.calories == 350
    assert recipe.fat == 20
    assert recipe.sugar == 50


def test_recipe_with_fixture(new_recipe):
    """
    checks if a recipe is initialized correctly
    uses fixture
    """
    assert new_recipe.name == 'testRecipe'
    assert new_recipe.calories == 350
    assert new_recipe.fat == 20
    assert new_recipe.sugar == 50