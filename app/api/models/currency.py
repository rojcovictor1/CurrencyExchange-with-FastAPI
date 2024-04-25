from pydantic import BaseModel


# Pydantic model for currency exchange requests
class CurrencyExchangeRequest(BaseModel):
    from_currency: str  # Currency to convert from (e.g., USD)
    to_currency: str  # Currency to convert to (e.g., EUR)
    amount: float = 1  # Amount of the initial currency to exchange (default is 1)


# Pydantic model for supported currency list
class CurrencyListResponse(BaseModel):
    currencies: dict  # Dictionary of supported currencies,
    # with keys as currency codes and values as descriptions


# Pydantic model for exchange rate information
class ExchangeRateResponse(BaseModel):
    rate: float  # Exchange rate between two currencies
