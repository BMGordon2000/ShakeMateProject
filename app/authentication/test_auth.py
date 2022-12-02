from app.DatabaseComponent import User

def test_auth():
    user = User('drake@gmail.com','drake12345')
    assert user.email == 'drake@gmail.com'
    assert user.password == 'drake12345'