from fastapi import Request
from app.services.auth.auth import decode_access_token

async def get_context(request: Request):
    user = None
    auth_header = request.headers.get("Authorization")
    if auth_header and auth_header.startswith("Bearer "):
        token = auth_header.removeprefix("Bearer ")
        print(f"Token received: {token}")  # Debugging line to check the token value
        payload = decode_access_token(token)
        if payload:
            user = payload  # dict with sub/username/email
        if(not token):
            print("No token provided in the Authorization header.")
            return {"request": request, "user": None}
    return {"request": request, "user": user}