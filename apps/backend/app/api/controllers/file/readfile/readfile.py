import pymupdf 
from app.api.controllers.file.chunking.chunking_file import split_text_into_chunks
from app.api.controllers.file.chunking.chunking_file import save_chunks_to_database
from app.api.controllers.file.embeddings_generation.embeddings_gen import embeddings_gen
import strawberry
from app.utils.auth.auth_utils import get_current_user
async def extract_pdf_text(path: str, document_id: str, info: strawberry.Info):
    # print("<-------------------extract_pdf_text controller called-------------------->\n\n\n\n")
    user =get_current_user(info)
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
    print("<-------------------All chunks generated-------------------->\n\n\n\n")
    await save_chunks_to_database(document_id=document_id, chunks=all_chunks, user_id=user["sub"])
    print("<-------------------All chunks saved to database-------------------->\n\n\n\n")
    await embeddings_gen(all_chunks)
    return {"pages": pages, "chunks": all_chunks}