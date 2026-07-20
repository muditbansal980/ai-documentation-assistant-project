from .embeddings_generation.emb_gen_client import gen_emb_client
from app.utils.auth.auth_utils import get_current_user
from app.models.client_message.client_message import ClientMessages
from app.db.session import AsyncSessionLocal
from app.api.controllers.llm.llm import generate_response
import uuid
import strawberry
from app.services.client_file_embeddings_matching.matching import ClientMessage_File_Matching
async def ClientMessage(message:str,docId:str,info:strawberry.Info):
    try:
        print("<-------------------ClientMessage controller called-------------------->\n\n\n\n")
        print("<-------------------ClientMessage controller called-------------------->")
        User = get_current_user(info)
        print("<-------------------User from token-------------------->\n\n\n\n")
        print("User:", User)
        print("<-------------------User from token-------------------->\n\n\n\n")
        ClientMess = message
        Id = str(uuid.uuid4())
        DocumentId = docId
        embeddings = await gen_emb_client(ClientMess) #list
        print("Embeddings generated for client message\n\n\n\n")
        async with AsyncSessionLocal() as session:
            Inserting = ClientMessages(
                Id= Id,
                DocId=DocumentId,
                UserId=User["sub"],
                Message=ClientMess,
                Embeddings = embeddings
            )
            # print("Inserting client message into database\n\n\n\n")
            session.add(Inserting)
            await session.commit()
        # print("Client message successfully embedded and inserted in db")
        
        # Call the ClientMessage_File_Matching function to match the client message with document chunks
        matching_result = await ClientMessage_File_Matching(docId=DocumentId, info=info, clientMsgEmb=embeddings)
        print("<-------------------Matching result-------------------->\n\n\n\n")
        print("Matching result(context):", matching_result)
        print("<-------------------Matching result-------------------->\n\n\n\n")
        context = [item[0] for item in matching_result[1]]
        providing_context = await generate_response(client_message=ClientMess, context=context)
        return {"message": "Client message successfully embedded and inserted in db and response generated"}
    except Exception as e:
        print("Error occured:-",e)