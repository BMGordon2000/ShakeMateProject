import pytest 
from app.DatabaseComponent import User
from app.__init__ import create_app

# @pytest.fixture
# def app():
#     app = create_app()
#     return app

# def test_favorites():
#     """
#     GIVEN a Flask application configured for testing
#     WHEN a user's favorite is added to the db
#     THEN check that the favorite is in the db
#     """
#     user = User('drake','drake@gmail.com','drake12345')
#     assert user.name == 'drake'
#     assert user.email == 'drake@gmail.com'
#     assert user.password == 'drake12345'