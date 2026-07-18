import jwt
import os
from dotenv import load_dotenv, find_dotenv
from datetime import datetime, timedelta, timezone
load_dotenv(find_dotenv()) 

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES") # 1 day

def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:

    to_encode = data.copy() # Copy the data to avoid modifying the original dictionary
    expire = datetime.now(timezone.utc) + (
        expires_delta or timedelta(minutes=int(JWT_ACCESS_TOKEN_EXPIRE_MINUTES))
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM) # Encode the token with the secret key and algorithm


def decode_access_token(token: str) -> dict | None:
    try:
        return jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None