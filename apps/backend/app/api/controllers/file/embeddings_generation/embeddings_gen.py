from sentence_transformers import SentenceTransformer
from app.db.session import AsyncSessionLocal
from app.models.file.chunks_of_file import DocumentChunks
from sqlalchemy import update

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
embeddings = []
async def embeddings_gen(chunks):
    print("Generating embeddings for all chunks...")
    for chunk in chunks:
        text = chunk["text"]
        embedding = model.encode(text)
        async with AsyncSessionLocal() as session:
            await session.execute(
                update(DocumentChunks)
                .where(
                    DocumentChunks.DocumentId == chunk["document_id"],
                    DocumentChunks.PageNumber == chunk["page"],
                    DocumentChunks.ChunkNumber == chunk["chunk_number"]
                )
                .values(
                Embedding=embedding.tolist()
            )
            )   
            await session.commit()
    chunk["embedding"] = embedding.tolist()  # Convert to list for JSON serialization
        
    print("Embeddings generated for all chunks.")
    # print("Modified chunks with embeddings:" + str(chunks))