import strawberry
from app.api.controllers.auth.register import login_user, register_user
from app.graphql.types import RegisterUserInput
from app.graphql.types import LoginUserInput
from app.graphql.types import UserType
from app.schemas.auth.register import UserRegisterSchema

@strawberry.type
class Mutation:
    @strawberry.mutation 
    async def RegisterUser(self, input: RegisterUserInput) -> UserType:
        print("RegisterUser mutation called")
        register_data = UserRegisterSchema(
            Username=input.Username,
            Email=input.Email,
            Password=input.Password,
        )
   # Call the register_user function from the controller
        result = await register_user(register_data)
        if "error" in result:
          raise Exception(result["error"])
      
        return UserType(
            Username=register_data.Username,
            Email=register_data.Email,
            Password=register_data.Password,
        )
    
    async def LoginUser(self,input: LoginUserInput) -> UserType:
        print("LoginUser mutation called")
        login_data = UserRegisterSchema(
            Email=input.Email,
            Password=input.Password,
        )
        result = await login_user(login_data)
        if "error" in result:
          raise Exception(result["error"])
      
        return UserType(
            Email=login_data.Email,
            Password=login_data.Password,
        )