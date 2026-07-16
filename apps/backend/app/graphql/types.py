import strawberry
@strawberry.input
class RegisterUserInput:
    Username: str
    Email: str
    Password: str
class LoginUserInput:
    Email: str
    Password: str
    
@strawberry.type
class UserType:
    Username: str
    Email: str
    Password: str
