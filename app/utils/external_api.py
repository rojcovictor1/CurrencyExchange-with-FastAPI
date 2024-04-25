import os
import requests
import dotenv
from fastapi import HTTPException


# Load environment variables from .env file
dotenv.load_dotenv()


# Get the API key from environment variables
API_KEY = os.getenv("API_KEY")


# Base URL for the external currency exchange data
BASE_URL = "https://api.apilayer.com/currency_data"


# Function to get the list of available currencies
def get_currency_list():
    response = requests.get(f"{BASE_URL}/list", headers={"apikey": API_KEY})
    if response.status_code != 200:
        raise HTTPException(
            status_code=500,
            detail="Failed to fetch currency list"
        )
    return response.json().get("currencies", {})


# Function to get the exchange rate for a given currency pair
def get_exchange_rate(from_currency: str, to_currency: str) -> dict:
    response = requests.get(
        f"{BASE_URL}/live",
        headers={"apikey": API_KEY},
        params={"currencies": f"{from_currency},{to_currency}"}
    )
    if response.status_code != 200:
        raise HTTPException(
            status_code=500,
            detail="Failed to fetch exchange rates"
        )
    return response.json().get("quotes", {})
