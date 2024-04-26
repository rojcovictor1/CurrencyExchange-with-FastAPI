from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
import jwt
from app.core.config import AppConfig

# Create an instance of AppConfig to access configuration values
config = AppConfig()

# Set up OAuth2 for token-based authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/")


# Function to create a JWT token with an optional expiration delta
def create_access_token(data: dict, expires_delta: timedelta = None):
    # Copy the data to ensure it isn't modified during processing
    to_encode = data.copy()
    # Determine the expiration time, defaulting to the configured value
    expire = datetime.utcnow() + (expires_delta or timedelta(
        minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES))
    # Add expiration to the data to be encoded
    to_encode.update({"exp": expire})
    # Encode the data into a JWT token using the secret key and algorithm
    encoded_jwt = jwt.encode(to_encode, config.SECRET_KEY, algorithm=config.ALGORITHM)
    return encoded_jwt


# Function to decode a JWT token and return its payload
def decode_access_token(token: str):
    try:
        # Decode the token using the secret key and algorithm
        payload = jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
        return payload
    except JWTError:
        # If there's an error decoding, raise an HTTP 401 (Unauthorized)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token or token expired",
            headers={"WWW-Authenticate": "Bearer"}
        )


# Function to get the current user from a JWT token
def get_current_user(token: str = Depends(oauth2_scheme)):
    # Decode the token to get the payload
    payload = decode_access_token(token)
    # Ensure the payload contains a 'sub' (subject) key
    if "sub" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token doesn't contain user information",
            headers={"WWW-Authenticate": "Bearer"}
        )
    # Return the subject, which typically represents the user ID or username
    return payload["sub"]
