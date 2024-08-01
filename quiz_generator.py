import streamlit as st

from document_processor import DocumentProcessor
from embedding_client import EmbeddingClient
from chroma_creator import ChromaCollectionCreator

if __name__ == "__main__":
    st.title("Quizzify")

    model_name = "textembedding-gecko@003"
    project = "YOUR-PROJECT-ID"
    location = "us-central1"
    
    processor = DocumentProcessor()
    processor.ingest_documents()
    embedding_client = EmbeddingClient(model_name, project, location)
    chroma_creator = ChromaCollectionCreator(processor, embedding_client)

    with st.form("quiz_generator"):
        st.subheader("Quiz Generator")
        topic = st.text_input("Enter the quiz topic...")
        amount = st.slider("How many questions would you like?", 1, 20)
        query = st.text_input("Enter your query...")
        generator_submitted = st.form_submit_button("Generate and Query")
        
        if generator_submitted:
            chroma_creator.create_collection()
            result = chroma_creator.query_collection(query)
