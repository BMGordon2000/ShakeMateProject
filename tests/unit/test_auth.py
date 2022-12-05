import pytest 
from app.DatabaseComponent import User
from app.__init__ import create_app

@pytest.fixture
def app():
    app = create_app()
    return app

def test_new_user():
    user = User('drake','drake@gmail.com','drake12345')
    assert user.name == 'drake'
    assert user.email == 'drake@gmail.com'
    assert user.password == 'drake12345'

def test_new_user_with_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email and password_hashed fields are defined correctly
    """
    assert new_user.name == 'drake'
    assert new_user.email == 'drake@gmail.com'
    assert new_user.password == 'drake12345'

def test_setting_password(new_user):
    """
    GIVEN an existing User
    WHEN the password for the user is set
    THEN check the password is stored correctly and not as plaintext
    """
    new_user.set_password('MyNewPassword')
    assert new_user.password != 'MyNewPassword'
    assert new_user.is_password_correct('MyNewPassword')
    assert not new_user.is_password_correct('MyNewPassword2')
    assert not new_user.is_password_correct('FlaskIsAwesome')

def test_existing_user():
    """
    GIVEN a User model
    WHEN a new User's email already exists for another user
    THEN check the email and password_hashed fields are defined correctly
    """
    user = User('Brian','drake@gmail.com','Brian12345')
    assert user.name == 'Brian'
    assert user.email == 'drake@gmail.com'
    assert user.password == 'Brian12345'
