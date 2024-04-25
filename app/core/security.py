import os
import dotenv
import jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError


dotenv.load_dotenv()
# Secret key for signing JWT. Keep it in an environment variable or configuration file
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
ALGORITHM = "HS256"  # Algorithm used to sign JWT
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time (30 minutes)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login/")


# Function to create a JWT token
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Function to decode a JWT token
def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token or token expired",
            headers={"WWW-Authenticate": "Bearer"},
        )


# Function to get user information from the JWT token
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if "sub" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token doesn't contain user information",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return payload["sub"]
