import pytest
from app import app

@pytest.fixture
def client():
    # Flask provides a test client for simulating requests
    with app.test_client() as client:
        yield client

def test_home_route(client):
    """Test that the home route returns the expected message"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello CI/CD with Docker!" in response.data
