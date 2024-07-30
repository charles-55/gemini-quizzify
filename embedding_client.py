import streamlit as st
from langchain_google_vertexai import VertexAIEmbeddings

class EmbeddingClient:
    def __init__(self, model_name, project, location):
        self.client = VertexAIEmbeddings(model_name=model_name, project=project, location=location)
    
    def embed_query(self, query):
        return self.client.embed_query(query)
    
    def embed_documents(self, documents):
        try:
            return self.client.embed_documents(documents)
        except AttributeError:
            print("Method embed_documents is not defined for the client.")
            return None

if __name__ == "__main__":
    st.title("Embedding Client")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    model_name = "textembedding-gecko@003"
    project = "YOUR-PROJECT-ID"
    location = "us-central1"
    
    embedding_client = EmbeddingClient(model_name, project, location)
    vectors = embedding_client.embed_query("Hello World!")
    if vectors:
        st.write(vectors)
        print("Successfully used the embedding client!")
