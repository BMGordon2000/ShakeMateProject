import pytest 
from app.DatabaseComponent import ingredients_table, recipe_table


from app.__init__ import create_app

@pytest.fixture
def app():
    app = create_app()
    return app


# These tests test User Story #4
def test_recipe_image():
    test_recipe1 = recipe_table(id=23)
    assert test_recipe1.id == 23