# Currency Exchange with FastAPI

This project is a FastAPI-based currency exchange application. It provides endpoints for user authentication, getting exchange rates, and performing currency conversions. The project uses JWT for authentication and integrates with an external currency data API for real-time exchange rates.

## Installation

1. **Clone the Repository**
   Clone the repository to your local environment using SSH or HTTPS:
   ```bash
   git clone git@github.com:rojcovictor1/CurrencyExchange-with-FastAPI.git
2. **Create a Virtual Environment**
    ```bash
   python -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate  # For Windows
3. **Install Dependencies**
    ```bash
   pip install -r requirements.txt
4. **Set Environment Variables**
   Ensure you have a .env file in the root of the project containing the necessary environment variables:
    ```bash
   SECRET_KEY=your_secret_key
    API_KEY=your_api_key

## Running the Project

1. **Start the FastAPI Server**
    Use Uvicorn to start the FastAPI server:
    ```bash
   uvicorn main:app --reload
2. **Access the API**
    The server runs on http://127.0.0.1:8000 by default. You can interact with the API using tools like Postman or Curl.

## API Endpoints

Here are some of the key API endpoints with example requests and expected responses:

### User Registration
- **Endpoint:** `/auth/register/`
- **Method:** `POST`
- **Request Body:** 
  ```json
  { "username": "example", "password": "mypassword" }
- **Response:**
    ```json
    { "message": "User registered successfully" }
  
### User Login
- **Endpoint:** `/auth/login/`
- **Method:** `POST`
- **Request Body:** 
  ```json
  { "username": "example", "password": "mypassword" }
- **Response:**
    ```json
    { "access_token": "your_token", "token_type": "Bearer" }
  
### Currency List
- **Endpoint:** `/currency/list/`
- **Method:** `GET`
- **Authorization:** 
  `Bearer <your_token>`
- **Response:**
    ```json
    { "currencies": { "USD": "United States Dollar", "EUR": "Euro" } }

### Currency Exchange
- **Endpoint:** `/currency/exchange/`
- **Method:** `POST`
- - **Request Body:** 
  ```json
  { "from_currency": "USD", "to_currency": "EUR", "amount": 1 }
- **Authorization:** 
  `Bearer <your_token>`
- **Response:**
    ```json
    { "rate": 0.85 }

## External API Integration

This project integrates with an external currency exchange API to fetch real-time exchange rates and currency information. The following external API was used:

- **API Name:** [Currency Data API](https://apilayer.com/marketplace/currency_data-api)
- **Provider:** APILayer
- **Endpoint Base URL:** `https://api.apilayer.com/currency_data`

To use this API, you need an API key, which can be obtained by registering for a free account on the [APILayer website](https://apilayer.com/). The API key should be stored in a `.env` file to ensure it's kept secure.

### Environment Variables

To work with the Currency Data API, ensure you have the following environment variable set in your `.env` file:

- `API_KEY`: Your unique API key for accessing the Currency Data API.

If you're sharing the code or the repository, make sure not to include sensitive information like API keys in the source code or commit history.

### API Limitations

- Note that the free plan for this API has limitations on the number of requests per month and may restrict some advanced features.
- Be aware of the terms of use and rate limits when integrating with this API.
## Contributing
If you'd like to contribute to this project, feel free to create a pull request or open an issue in the GitHub repository.

## Contact
For questions or support, contact rojcovictor1@gmail.com.