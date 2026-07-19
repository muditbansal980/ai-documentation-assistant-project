import strawberry
from app.graphql.types import AuthError
from typing import Union, Annotated
from app.graphql.types import MessageResponse
from app.api.controllers.file.upload_file import UploadFile
from app.utils.auth.auth_utils import get_current_user
from strawberry.file_uploads import Upload
@strawberry.type
class FileMutation:
    UploadFileResult = Annotated[
        Union[MessageResponse, AuthError],
        strawberry.union("UploadFileResult"),
    ]
    @strawberry.mutation
    async def UploadFile(self,info:strawberry.Info,file:Upload) ->UploadFileResult:
        user = get_current_user(info)
        if not user:
            return AuthError()  # uses default "Not authenticated" message
        controller = await UploadFile(file,user)
        if controller.error:
           return AuthError(message=controller.error, statusCode=400)
        return MessageResponse(
            message="File uploaded successfully."
        )
    