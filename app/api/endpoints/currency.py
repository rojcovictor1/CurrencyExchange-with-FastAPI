from fastapi import APIRouter, HTTPException, Depends

from app.api.models.currency import CurrencyListResponse, ExchangeRateResponse, \
    CurrencyExchangeRequest
from app.utils.external_api import get_currency_list, get_exchange_rate
from app.core.security import get_current_user

router = APIRouter()


# Endpoint to get a list of available currencies
@router.get("/currency/list/", response_model=CurrencyListResponse)
def list_currencies(_user: str = Depends(get_current_user)):
    currencies = get_currency_list()
    return {"currencies": currencies}


# Endpoint to convert currencies
@router.post("/currency/exchange/", response_model=ExchangeRateResponse,
             dependencies=[Depends(get_current_user)])
def exchange_currency(request: CurrencyExchangeRequest):  # Using Pydantic model for input
    exchange_rate = get_exchange_rate(request.from_currency, request.to_currency)
    if not exchange_rate:
        raise HTTPException(
            status_code=400,
            detail="Invalid currency code or rate not available"
        )

    rate_key = f"{request.from_currency}{request.to_currency}"
    if rate_key not in exchange_rate:
        raise HTTPException(
            status_code=400,
            detail=f"No exchange rate found for {request.from_currency} to {request.to_currency}"
        )

    rate = exchange_rate[rate_key]
    return {"rate": rate}
