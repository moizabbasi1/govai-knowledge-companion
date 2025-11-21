
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
CHROMA_DIR = os.path.join(BASE_DIR, "chroma_db")
MODEL_NAME = "llama3.1:8b"  # Ollama model name
TOP_K = 4
CHUNK_SIZE = 400
CHUNK_OVERLAP = 50
