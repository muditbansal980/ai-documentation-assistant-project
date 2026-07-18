import strawberry
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