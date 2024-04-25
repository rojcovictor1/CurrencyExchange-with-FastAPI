from fastapi import FastAPI
from app.api.endpoints import users, currency

app = FastAPI()

# Include the users endpoints
app.include_router(users.router)
app.include_router(currency.router)
