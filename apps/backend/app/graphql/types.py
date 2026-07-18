import strawberry
from typing import Optional

@strawberry.type
class AuthError:
    message: str = "Not authenticated"
    statusCode: int = 401  # Default status code for authentication errors    
@strawberry.input
class RegisterUserInput:
    Username: str
    Email: str
    Password: str
@strawberry.input
class LoginUserInput:
    Email: str
    Password: str
    
@strawberry.type
class UserType:
    Username: str
    Email: str
    Password: str
  
@strawberry.type
class UserLoginType:
    Email: str
    Password: str  
    authToken: str = None  # Optional field for the auth token

@strawberry.type
class MessageResponse:
    message: str
    error:Optional[str] = None # Optional field for error messages
  # Optional field for error messages