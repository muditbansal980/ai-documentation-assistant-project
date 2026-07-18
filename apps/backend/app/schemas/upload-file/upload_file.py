from pydantic import BaseModel
class UploadFileSchema(BaseModel):
    UserId:str
    OriginalFileName:str
    StoragePath:str
    MimeType:str
    FileSize:int
    Status:str