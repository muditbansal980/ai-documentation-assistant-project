import pymupdf 
async def extract_pdf_text(path: str):

    document = pymupdf.open(path)
    text = ""
    pages = []
    for page_number, page in enumerate(document):
    
        pages.append(
            {
                "page": page_number + 1,
                "text": page.get_text()
            }
        )
    return pages