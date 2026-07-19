import strawberry
from app.graphql.types import AuthError
from typing import Union, Annotated
from app.graphql.types import MessageResponse
from app.utils.auth.auth_utils import get_current_user
from app.api.controllers.clientmessage.clientmessage import ClientMessage
@strawberry.type

class ClientMessageMutation:
    ClientMessageResult = Annotated[Union[MessageResponse, AuthError], strawberry.union("ClientMessageResult")]
    @strawberry.mutation 
    async def ClientMessage(self,info:strawberry.Info,message:str,documentId:str) -> ClientMessageResult:
        user = get_current_user(info)
        if not user:
            print("<-------------------No user error-------------------->\n\n\n\n")
            print("<-------------------No user error-------------------->")
            return AuthError()  # uses default "Not authenticated" message
        print("<-------------------Data from frontend-------------------->\n\n\n\n")
        print("message:", message)
        print("documentId:", documentId)
        print("<-------------------Data from frontend-------------------->\n\n\n\n")
        ClientMess = str(message)
        ClientMess.replace(" ","")
        if(ClientMess == ""):
            print("<-------------------No message error-------------------->\n\n\n\n")
            print("<-------------------No message error-------------------->")
            return AuthError(
                message="Hey I think you forgot the message",
                statusCode=400
            )
        else: 
            print("<-------------------ClientMessage controller called-------------------->\n\n\n\n")
            print("<-------------------ClientMessage controller called-------------------->")
            controller = await ClientMessage(message=ClientMess,docId=documentId,info=info) 
            
        return MessageResponse(
            message="Client message processed successfully."
        )