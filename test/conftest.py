import pytest
from app import app

@pytest.fixture(scope='module')
def client():
    with app.test_client() as client:
        yield client
