from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.models.file.chunks_of_file import DocumentChunks
from app.db.session import AsyncSessionLocal
import uuid
def split_text_into_chunks(text: str):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=50
    )
    chunks = splitter.split_text(text)
    
    return chunks

async def save_chunks_to_database(document_id: str, chunks: list, user_id: str):
    for chunk in chunks:
        async with AsyncSessionLocal() as session:
            chunk_record =DocumentChunks(
                Id=str(uuid.uuid4()),
                DocumentId=document_id,
                UserId=user_id,
                PageNumber=chunk["page"],
                ChunkNumber=chunk["chunk_number"],  
                ChunkText=chunk["text"]
            )
            session.add(chunk_record)
            await session.commit()
            
        