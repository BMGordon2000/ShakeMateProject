
import pytest 
from app.DatabaseComponent import User




from app.__init__ import create_app

@pytest.fixture
def app():
    app = create_app()
    return app



def test_new_user():
    user = User('drake@gmail.com','drake12345')
    assert user.email == 'drake@gmail.com'
    assert user.password == 'drake12345'
    assert user.is_authenticated
    assert user.is_active
    assert not user.is_anonymous


def test_new_user_with_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email and password_hashed fields are defined correctly
    """
    assert new_user.email == 'drake@gmail.com'
    assert new_user.password == 'drake12345'
