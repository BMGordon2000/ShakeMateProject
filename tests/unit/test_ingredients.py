import pytest 
from app.DatabaseComponent import ingredients_table


from app.__init__ import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

def test_new_ingredient_1():
    test_ingredient1 = ingredients_table(name='WatermelonTest')
    assert test_ingredient1.name == 'WatermelonTest'

def test_new_ingredient_2():
    test_ingredient2 = ingredients_table(name='@')
    assert test_ingredient2.name == '@'

def test_new_ingredient_3():
    test_ingredient3 = ingredients_table(name='12376128731263871263128361273612783612736123612371283612836127361732169')
    assert test_ingredient3.name == '12376128731263871263128361273612783612736123612371283612836127361732169'