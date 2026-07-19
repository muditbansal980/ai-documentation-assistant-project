from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
embeddings = []
def embeddings_gen(chunks):
    for chunk in chunks:
        text = chunk["text"]
        embedding = model.encode(text)
        chunk["embedding"] = embedding.tolist()  # Convert to list for JSON serialization
        
    print("Embeddings generated for all chunks.")
    # print("Modified chunks with embeddings:" + str(chunks))