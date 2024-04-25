from fastapi import APIRouter, HTTPException, status, Depends
from datetime import timedelta

from app.api.models.user import UserCreate
from app.core.security import create_access_token, get_current_user

import bcrypt

router = APIRouter()


# Dictionary to store registered users
users_db = {}


# Endpoint for user registration
@router.post("/auth/register/")
def register_user(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )

    # Hash the user's password
    hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())
    users_db[user.username] = hashed_password
    return {"message": "User registered successfully"}


# Endpoint for user login and JWT token generation
@router.post("/auth/login/")
def login_user(user: UserCreate):
    if user.username not in users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username or password",
        )

    # Verify the password
    hashed_password = users_db[user.username]
    if not bcrypt.checkpw(user.password.encode("utf-8"), hashed_password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid username or password",
        )

    # Generate JWT token
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "Bearer"}


# Endpoint to retrieve current user's information
@router.get("/auth/me/")
def get_current_user_info(user: str = Depends(get_current_user)):
    return {"username": user}
