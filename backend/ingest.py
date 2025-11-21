
import os, textwrap, json
# For this demo we read from a plaintext file, but this script can be extended to PDFs.
def load_text(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

def chunk_text(text, chunk_size=400, overlap=50):
    tokens = text.split()
    chunks = []
    i = 0
    while i < len(tokens):
        chunk = tokens[i:i+chunk_size]
        chunks.append(' '.join(chunk))
        i += chunk_size - overlap
    return chunks

if __name__ == '__main__':
    src = os.path.join(os.path.dirname(__file__), '..', 'privacy_act_excerpt.txt')
    text = load_text(src)
    chunks = chunk_text(text, 200, 30)
    for idx, c in enumerate(chunks):
        print(f'--- CHUNK {idx} ---')
        print(c[:500])
