from pydantic import ValidationError
from app.api.models.user import UserCreate
from app.api.models.currency import (
    CurrencyExchangeRequest,  # Model for currency exchange requests
    CurrencyListResponse,  # Model for list of supported currencies
    ExchangeRateResponse  # Model for exchange rate information
)


# Test for valid user creation model
def test_user_create_valid():
    # Create a valid user instance
    user = UserCreate(username="validuser", password="securepassword")
    assert user.username == "validuser"  # Ensure the username is correct
    assert user.password == "securepassword"  # Ensure the password is correct


# Test for invalid user creation model
def test_user_create_invalid():
    # Test invalid data (empty username and password)
    try:
        UserCreate(username="", password="")  # Should raise a validation error
    except ValidationError as e:
        # Ensure the error message indicates the missing field
        assert e.errors()[0]["msg"] == "field required"


# Test for valid currency exchange request model
def test_currency_exchange_request_valid():
    # Create a valid currency exchange request
    exchange_request = CurrencyExchangeRequest(
        from_currency="USD",
        to_currency="EUR",
        amount=1
    )
    assert exchange_request.from_currency == "USD"  # Validate source currency
    assert exchange_request.to_currency == "EUR"  # Validate target currency
    assert exchange_request.amount == 1  # Validate amount for exchange


# Test for invalid currency exchange request model
def test_currency_exchange_request_invalid():
    # Test with invalid data
    try:
        CurrencyExchangeRequest(
            from_currency="",  # Empty source currency
            to_currency="",  # Empty target currency
            amount=0  # Invalid amount
        )
    except ValidationError as e:
        # Ensure validation error occurs for missing fields
        assert e.errors()[0]["msg"] == "field required"


# Test for valid currency list response model
def test_currency_list_response_valid():
    # Create a valid currency list response
    currencies = {"USD": "United States Dollar", "EUR": "Euro"}
    currency_list = CurrencyListResponse(currencies=currencies)
    assert "USD" in currency_list.currencies  # Validate key in the dictionary
    assert currency_list.currencies["USD"] == "United States Dollar"  # Validate description
    assert currency_list.currencies["EUR"] == "Euro"  # Validate another description


# Test for valid exchange rate response model
def test_exchange_rate_response_valid():
    # Create a valid exchange rate response
    rate_response = ExchangeRateResponse(rate=1.12)
    assert rate_response.rate == 1.12  # Validate the exchange rate value
