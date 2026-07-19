from sentence_transformers import SentenceTransformer
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)
client_embeddings = []
async def gen_emb_client(message:str):
    print("<-------------------Generating embeddings for client message-------------------->\n\n\n\n")
    embedding = model.encode(message)
    return embedding.tolist()