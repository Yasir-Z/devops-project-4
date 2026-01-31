import pytest
from app import app, calculate_priority


# --- Unit Tests ---
def test_calculate_priority_high():
    assert calculate_priority(10) == "High"


def test_calculate_priority_medium():
    assert calculate_priority(3) == "Medium"


def test_calculate_priority_low():
    assert calculate_priority(0) == "Low"


# --- Integration Tests ---
@pytest.fixture
def client():
    """Configures the app for testing."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_api_status_endpoint(client):
    """Tests if the API route returns the correct JSON and status code."""
    response = client.get("/status")
    data = response.get_json()

    assert response.status_code == 200
    assert data["status"] == "Active"
    assert data["priority"] == "Medium"
