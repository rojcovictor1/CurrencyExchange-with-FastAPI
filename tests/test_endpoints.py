from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# Test for user registration endpoint
def test_register_user():
    response = client.post("/auth/register/",
                           json={"username": "newuser", "password": "password123"})
    assert response.status_code == 200  # Ensure status code is 200 (success)
    assert response.json() == {
        "message": "User registered successfully"}  # Verify response content


# Test for user login endpoint
def test_login_user():
    # Register the user first to ensure the account exists
    client.post("/auth/register/", json={
        "username": "newuser", "password": "password123"})

    response = client.post("/auth/login/", json={
        "username": "newuser", "password": "password123"})
    assert response.status_code == 200  # Successful login
    assert "access_token" in response.json()  # JWT token should be in response


# Test for currency exchange endpoint
def test_currency_exchange():
    # Log in to get the access token
    login_response = client.post("/auth/login/",
                                 json={"username": "newuser", "password": "password123"})
    access_token = login_response.json()["access_token"]

    # Test valid currency exchange
    response = client.post(
        "/currency/exchange/",
        headers={"Authorization": f"Bearer {access_token}"},
        json={"from_currency": "USD", "to_currency": "EUR"}
    )
    assert response.status_code == 200  # Successful exchange
    assert "rate" in response.json()  # Verify response has exchange rate
