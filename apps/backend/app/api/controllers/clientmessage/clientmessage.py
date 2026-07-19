from .embeddings_generation.emb_gen_client import gen_emb_client
from app.utils.auth.auth_utils import get_current_user
from app.models.client_message.client_message import ClientMessages
from app.db.session import AsyncSessionLocal
import uuid
import strawberry
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
            print("Inserting client message into database\n\n\n\n")
            session.add(Inserting)
            await session.commit()
        print("Client message successfully embedded and inserted in db")
    except Exception as e:
        print("Error occured:-",e)