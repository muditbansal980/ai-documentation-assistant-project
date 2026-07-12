from pydantic import BaseModel
class UserRegisterSchema(BaseModel):
    Username:str
    Email:str
    Password:str