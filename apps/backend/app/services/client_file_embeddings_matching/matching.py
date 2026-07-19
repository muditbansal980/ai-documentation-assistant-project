from sqlalchemy import text
import strawberry

from app.utils.auth.auth_utils import get_current_user
from app.db.session import AsyncSessionLocal
async def ClientMessage_File_Matching(
    docId: str,
    info: strawberry.Info,
    clientMsgEmb: list
):

    try:

        user = get_current_user(info)

        async with AsyncSessionLocal() as session:

            result = await session.execute(
                text("""
                    SELECT
                        dc."ChunkText",
                        dc."PageNumber",
                        dc."ChunkNumber",
                        dc."Embedding" <=> CAST(:embedding AS vector)
                            AS similarity
                    FROM "DocumentChunks" dc
                    JOIN "Document" d
                        ON dc."DocumentId" = d."Id"
                    WHERE
                        dc."DocumentId" = :docId
                        AND d."UserId" = :userId
                    ORDER BY similarity
                """),
                {
                    "docId": docId,
                    "userId": user["sub"],
                    "embedding": str(clientMsgEmb)
                }
            )

            chunks = result.fetchall()
            print("<-------------------Matching result-------------------->\n\n\n\n")
            print("Matching result:", chunks)
            print("<-------------------Matching result-------------------->\n\n\n\n")
            return [
                {
                    "text": chunk.ChunkText,
                    "page": chunk.PageNumber,
                    "chunk": chunk.ChunkNumber,
                    "distance": chunk.similarity
                }
                for chunk in chunks
            ]

    except Exception as e:
        print(e)