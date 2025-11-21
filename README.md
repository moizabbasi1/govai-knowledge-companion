# GovAI Knowledge Companion

A local, privacy-preserving Retrieval-Augmented Generation (RAG) system designed for government workflows. This project loads documents, builds vector embeddings, indexes them with ChromaDB, and answers user questions using an on-device Llama model via **Ollama**.

This README includes:

* 🚀 Project Overview
* 📂 Recommended Folder Structure
* 🛠️ Installation Steps
* ▶️ How to Run the Project
* 🔧 Troubleshooting

---

## 🚀 Project Overview

The GovAI Knowledge Companion is a secure RAG application designed for government environments where cloud-based LLMs cannot be used. All processing—including embeddings, retrieval, and generation—runs **fully local** using:

* **Ollama** (local LLM serving)
* **Llama 3.1 (8B)** or any compatible model
* **ChromaDB** for vector storage
* **Streamlit** for the frontend UI

This allows government employees to upload or index policy documents and ask natural-language questions with chunk-level citations.

---

## 📂 Recommended Folder Structure

Below is the clean, standardized structure for your repo. You can update your project to match this layout.

```
govai-knowledge-companion/
│
├── backend/
│   ├── __init__.py
│   ├── config.py
│   ├── embed.py
│   ├── llm.py
│   └── rag.py
│
├── scripts/
│   ├── build_index.py
│   └── ingest_docs.py
│
├── ui/
│   ├── app.py            # Streamlit UI
│   └── __init__.py
│
├── data/
│   ├── raw/              # Original source documents
│   └── processed/        # Chunked text
│
├── chroma/               # Auto-created by ChromaDB
│
├── README.md
├── requirements.txt
└── .gitignore
```

If you'd like, I can auto-generate all missing folders and files.

---

## 🛠️ Installation Instructions

Follow these steps to install and run your project on Windows/macOS/Linux.

### 1️⃣ Clone the repo

```
git clone https://github.com/<your-username>/govai-knowledge-companion.git
cd govai-knowledge-companion
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 🦙 Install and Run Ollama

### Install Ollama

* Download from [https://ollama.com](https://ollama.com)

### Pull the Llama Model

```
ollama pull llama3.1:8b
```

### Start the Ollama Server

```
ollama serve
```

*(Must be running in a separate terminal window.)*

---

## 📚 Build the Embedding Index

Before running the UI, you must build the vector database.

```
python -m scripts.build_index
```

This processes your documents → chunks → embeddings → Chroma index.

---

## ▶️ Run the Streamlit App

```
streamlit run ui/app.py
```

The app launches here:

```
http://localhost:8501
```

---

## 🔧 Troubleshooting

### **Ollama Port Already in Use**

```
netstat -ano | findstr 11434
```

Then kill the process:

```
taskkill /PID <PID> /F
```

### **ModuleNotFoundError: No module named 'backend'**

Make sure:

* `backend/` has `__init__.py`
* You are running from project root:

```
python -m ui.app
```

Or use Streamlit:

```
streamlit run ui/app.py
```

### **Ollama Client Errors**

Use the updated API:

```
response = ollama.generate(model=model, prompt=prompt)
```

### **Slow Generation**

Running locally means:

* Llama 8B uses CPU by default on most Windows machines
* For GPU acceleration, enable CUDA or use WSL2
