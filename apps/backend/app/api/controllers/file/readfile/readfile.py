import pymupdf 
from app.api.controllers.file.chunking.chunking_file import split_text_into_chunks
from app.api.controllers.file.chunking.chunking_file import save_chunks_to_database
from app.api.controllers.file.embeddings_generation.embeddings_gen import embeddings_gen
async def extract_pdf_text(path: str, document_id: str):

    document = pymupdf.open(path)
    text = ""
    pages = []
    all_chunks = []
    for page_number, page in enumerate(document):
    
        pages.append(
            {
                "page": page_number + 1,
                "text": page.get_text(),
            }
        )
        chunks = split_text_into_chunks(
        page.get_text()
       )
        for index, chunk in enumerate(
        chunks,
        start=1
        ):
            all_chunks.append(
                {
                    "page": page_number + 1,
                    "chunk_number": index,
                    "text": chunk,
                    "document_id": document_id
                }
            )
    await save_chunks_to_database(document_id=document_id, chunks=all_chunks)
    await embeddings_gen(all_chunks)
    return {"pages": pages, "chunks": all_chunks}