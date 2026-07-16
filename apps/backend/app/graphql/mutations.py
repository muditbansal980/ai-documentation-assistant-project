import strawberry
from app.api.controllers.auth.register import login_user, register_user
from app.graphql.types import RegisterUserInput, UserLoginType
from app.graphql.types import LoginUserInput
from app.graphql.types import UserType
from app.schemas.auth.register import UserRegisterSchema,UserLoginSchema

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
    @strawberry.mutation
    async def LoginUser(self,input: LoginUserInput) -> UserLoginType:
        print("LoginUser mutation called")
        login_data = UserLoginSchema(
            Email=input.Email,
            Password=input.Password,
        )
        result = await login_user(login_data)
        if "error" in result:
          raise Exception(result["error"])
      
        return UserLoginType(
            Email=login_data.Email,
            Password=login_data.Password,
        )