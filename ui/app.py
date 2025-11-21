
import streamlit as st
from backend import rag

st.set_page_config(page_title='GovAI Knowledge Companion', layout='wide')

st.title('GovAI Knowledge Companion — Demo')
st.markdown('Ask questions about the Privacy Act excerpt. Responses include citations to chunk IDs.')

question = st.text_input('Ask a question:', 'What is "personal information" defined as?')

if st.button('Ask'):
    with st.spinner('Retrieving and generating answer...'):
        result = rag.answer(question)
    parsed = result.get('parsed', {})
    st.subheader('Answer')
    st.write(parsed.get('answer') or result.get('raw'))
    st.subheader('Citations (retrieved chunks)')
    retrieved = result.get('retrieved', [])
    for r in retrieved:
        st.markdown(f"**Chunk ID:** {r['metadata'].get('chunk_id')}  \n{r['document'][:600]}...")
    st.subheader('Explanation')
    st.write(parsed.get('explanation', 'No explanation parsed.'))

st.sidebar.header('Demo Controls')
k = st.sidebar.slider('Top-k retrieval', 1, 8, 4)
st.sidebar.markdown('Make sure you ran `python scripts/build_index.py` to create the index.')
