# query for getting conversational messages
from sqlalchemy import text,select
import strawberry
from app.models.conversation_messages.conversational_messages import ConversationalMessages
from app.models.file.upload_file import Document
from app.graphql.types import ConversationalMessageType,DocumentType
from app.db.session import AsyncSessionLocal
from app.utils.auth.auth_utils import get_current_user

@strawberry.type
class Query:

    @strawberry.field
    def get_conversational_messages(self, docId: str,info: strawberry.Info) -> list[ConversationalMessageType]:
        print("<-------------------Fetching messages from database-------------------->\n\n\n\n")
        print("Document ID:", docId)
        print("<-------------------Fetching messages from database-------------------->\n\n\n\n")
        async def get_messages():
            user = get_current_user(info)
            async with AsyncSessionLocal() as session:
                stmt = (
                    select(ConversationalMessages)
                    .where(
                                ConversationalMessages.DocId == docId,
                                ConversationalMessages.UserId == user["sub"],
                            )
                            .order_by(ConversationalMessages.CreatedAt.asc())
                        )
                result = await session.execute(stmt)
                rows = result.scalars().all()
                print("<-------------------Fetched messages from database-------------------->\n\n\n\n")
                print("Messages:", rows)
                print("<-------------------Fetched messages from database-------------------->\n\n\n\n")
                # return [ConversationalMessages(**dict(row)) for row in rows]
                return rows

        return get_messages()
    @strawberry.field
    def get_all_documents_user(self,info: strawberry.Info) -> list[DocumentType]:
        async def get_documents():
            user = get_current_user(info)
            async with AsyncSessionLocal() as session:
                stmt = (
                    select(Document.Id, Document.OriginalFileName, Document.UserId)
                    .where(
                                Document.UserId == user["sub"],
                            )
                            .distinct()
                        )
                result = await session.execute(stmt)
                rows = result.all()
                print("<-------------------Fetched documents from database-------------------->\n\n\n\n")
                print("Documents:", rows)
                print("<-------------------Fetched documents from database-------------------->\n\n\n\n")
                return rows

        return get_documents()