import pytest

from app import create_app, db


@pytest.fixture()
def app():
    app = create_app()  # "sqlite://" inside parenthesis potentially? 
    yield app
    # return app

    with app.app_context():
        db.create_all


@pytest.fixture()
def client(app):
    return app.test_client()
