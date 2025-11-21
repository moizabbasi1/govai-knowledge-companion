import os
from sentence_transformers import SentenceTransformer
import chromadb
from backend import config

def create_client(persist_directory=None):
    persist_directory = persist_directory or config.CHROMA_DIR
    # New PersistentClient API
    client = chromadb.PersistentClient(path=persist_directory)
    return client

def embed_and_index(chunks, metadatas):
    # 1️⃣ Create embeddings
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks, show_progress_bar=True, convert_to_numpy=True)

    # 2️⃣ Create or connect to Chroma client
    client = create_client()
    collection = client.get_or_create_collection(name='govai_demo')

    # 3️⃣ Generate unique IDs for each chunk
    ids = [str(i) for i in range(len(chunks))]

    # 4️⃣ Add documents to collection
    collection.add(
        ids=ids,
        documents=chunks,
        metadatas=metadatas,
        embeddings=embeddings.tolist()
    )

    return collection


if __name__ == '__main__':
    from backend.ingest import chunk_text, load_text
    src = os.path.join(os.path.dirname(__file__), '..', 'privacy_act_excerpt.txt')
    text = load_text(src)
    chunks = chunk_text(text, 200, 30)
    metadatas = [{'chunk_id': i} for i in range(len(chunks))]
    embed_and_index(chunks, metadatas)
    print('Indexed', len(chunks), 'chunks')
