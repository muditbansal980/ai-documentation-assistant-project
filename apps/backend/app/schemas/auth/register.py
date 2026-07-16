from pydantic import BaseModel
class UserRegisterSchema(BaseModel):
    Username:str
    Email:str
    Password:str
class UserLoginSchema(BaseModel):
    Email:str
    Password:str