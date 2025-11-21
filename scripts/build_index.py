
from backend.ingest import chunk_text, load_text
from backend.embed import embed_and_index
import os

src = os.path.join(os.path.dirname(__file__), '..', 'privacy_act_excerpt.txt')
text = load_text(src)
chunks = chunk_text(text, 200, 30)
metadatas = [{'chunk_id': i, 'source': 'privacy_act_excerpt'} for i in range(len(chunks))]
embed_and_index(chunks, metadatas)
print('Indexing complete.')
