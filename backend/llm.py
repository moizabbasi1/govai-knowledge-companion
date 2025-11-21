import ollama
from backend import config
import json

def call_llama_system(prompt):
    """
    Uses the current Ollama Python client.
    """
    model = config.MODEL_NAME

    response = ollama.generate(
        model=model,
        prompt=prompt,
        options={
            "temperature": 0,
            "num_predict": 512  # max tokens replacement
        }
    )

    # response = {'model': ..., 'created_at': ..., 'response': 'text here'}
    return response.get("response", "")
    

def build_rag_prompt(question, retrieved_chunks):
    instruction = (
        "You are an assistant helping a government employee. "
        "Answer the question using ONLY the provided source excerpts. "
        "Provide a concise answer, and then list the exact chunk IDs you used as citations.\n\n"
        "--- SOURCES:\n"
    )
    for i, c in enumerate(retrieved_chunks):
        instruction += f"CHUNK_{c['metadata'].get('chunk_id', i)}:\n{c['document'][:800]}\n\n"
    instruction += (
        f"\nQUESTION: {question}\n\n"
        "Answer with a short answer followed by a JSON object with keys: "
        "answer, citations, explanation."
    )
    return instruction


def parse_llama_output(text):
    import re, json
    match = re.search(r'(\{[\s\S]*\})\s*$', text)
    if match:
        try:
            return json.loads(match.group(1))
        except:
            pass
    return {"answer": text, "citations": [], "explanation": ""}
