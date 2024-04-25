from fastapi import FastAPI
from app.api.endpoints import users

app = FastAPI()

# Include the users endpoints
app.include_router(users.router)
