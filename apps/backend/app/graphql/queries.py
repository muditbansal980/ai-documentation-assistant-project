# query for getting conversational messages
import strawberry
from app.models.conversation_messages.conversational_messages import ConversationalMessages
from app.graphql.types import ConversationalMessageType
from app.db.session import AsyncSessionLocal
from app.utils.auth.auth_utils import get_current_user

@strawberry.type
class Query:

    @strawberry.field
    def get_conversational_messages(self, docId: str,info: strawberry.Info) -> list[ConversationalMessageType]:
        async def get_messages():
            user = get_current_user(info)
            async with AsyncSessionLocal() as session:
                result = await session.execute(
                    f"SELECT * FROM ConversationalMessages WHERE DocId = '{docId}' && UserId = '{user['sub']}' ORDER BY Id DESC"
                )
                messages = result.fetchall()
                print("<-------------------Fetched messages from database-------------------->\n\n\n\n")
                print("Messages:", messages)
                print("<-------------------Fetched messages from database-------------------->\n\n\n\n")
                return [ConversationalMessages(**dict(row)) for row in messages]
            

        return get_messages()