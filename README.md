# GovAI Knowledge Companion — Demo Project

This repository contains a **demo** implementation of the GovAI Knowledge Companion (RAG-powered) using **Llama 3.1 (via Ollama)**, **Sentence-Transformers embeddings**, **Chroma** vector store, and a **Streamlit** frontend.

## What this demo includes
- Document ingestion and chunking scripts
- Embedding and Chroma indexing script
- Simple RAG query flow that retrieves top-k chunks and calls Llama via Ollama
- Streamlit UI to interact with the system
- Sample document: `privacy_act_excerpt.txt` (small excerpt for demo)

## Prerequisites
- Python 3.10+
- [Ollama](https://ollama.com/) installed and running locally
  - Pull Llama model: `ollama pull llama3.1:8b` (or another compatible model)
- Create and activate a Python virtual environment, then install requirements:
```
python -m venv .venv
source .venv/bin/activate    # macOS / Linux
.venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Quick setup (one-time)
1. Index the demo document:
```
python scripts/build_index.py
```
2. Launch the Streamlit UI:
```
streamlit run ui/app.py
```

## Notes on Ollama
This demo expects Ollama to be available locally. The `ollama` Python package is used to communicate with the local Ollama daemon. Make sure Ollama is running (by launching the Ollama app or running the Ollama daemon) and the model (e.g., `llama3.1:8b`) is pulled.

## Security & Responsible AI
- This demo runs entirely locally — no data leaves your machine.
- The demo provides simple citation output (chunk metadata) to support explainability.
- For production use, deploy inside a secure, audited environment and add bias checks, logging, access control, and human-in-the-loop validation as described in the submission.

## Project structure
```
govai-knowledge-companion/
├── backend/
│   ├── ingest.py
│   ├── embed.py
│   ├── rag.py
│   ├── llm.py
│   └── config.py
├── ui/
│   └── app.py
├── scripts/
│   └── build_index.py
├── privacy_act_excerpt.txt
├── requirements.txt
└── README.md
```