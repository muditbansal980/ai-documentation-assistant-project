
import uuid
from strawberry.file_uploads import Upload
from app.graphql.types import MessageResponse
from app.db.session import AsyncSessionLocal
from app.models.file.upload_file import Document
from app.api.controllers.file.readfile.readfile import extract_pdf_text
async def UploadFile(file:Upload,user:dict):
    try:
        # Save the file metadata to the database
        content = await file.read()  # read once
        documentId = str(uuid.uuid4())  # Generate a unique ID for the document
        async with AsyncSessionLocal() as session:
            document = Document(
                Id = documentId,
                UserId = user["sub"],  # Using the user ID from the decoded token
                OriginalFileName = file.filename,
                StoragePath = f"uploads/{file.filename}",
                MimeType = file.content_type,   
                FileSize=len(content),
                Status = "PENDING"
            ) 
            session.add(document)
            await session.commit()
            # Save the file to the specified path
            path = f"uploads/{file.filename}"
            with open(path, "wb") as f:
                # f.write(await file.read())
                f.write(content)  # write the content read earlier
            # Extract text from the uploaded PDF
            extracted_text = await extract_pdf_text(path, documentId)
            # print(f"Extracted text from {file.filename}: {extracted_text}")
            print(
                extracted_text["chunks"][0]
            )
            return MessageResponse(
                message="File uploaded successfully."
            )
            
    except Exception as e:
        return MessageResponse(
            message="File upload failed.",
            error=str(e)
        )