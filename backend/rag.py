
import os, json
from backend import config
from backend.embed import create_client
from backend.llm import build_rag_prompt, call_llama_system, parse_llama_output

def retrieve(query, k=None):
    k = k or config.TOP_K
    client = create_client()
    collection = client.get_or_create_collection('govai_demo')
    # Note: chroma client returns dictionary-like results for query
    results = collection.query(query_texts=[query], n_results=k)
    docs = []
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        docs.append({'document': doc, 'metadata': meta})
    return docs

def answer(query):
    retrieved = retrieve(query)
    prompt = build_rag_prompt(query, retrieved)
    text = call_llama_system(prompt)
    parsed = parse_llama_output(text)
    # Attach retrieved metadata for UI
    return {'raw': text, 'parsed': parsed, 'retrieved': retrieved}
