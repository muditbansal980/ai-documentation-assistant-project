from pydantic import BaseModel
class UserLoginSchema(BaseModel):
    Email:str
    Password:str