import streamlit as st
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.vectorstores import Chroma

from document_processor import DocumentProcessor
from embedding_client import EmbeddingClient

class ChromaCollectionCreator:
    def __init__(self, processor, embedding_client):
        self.processor = processor
        self.embedding_client = embedding_client
        self.db = None
        self.page_contents = []

    def create_collection(self):
        if len(self.processor.documents) == 0:
            st.error("No documents found!", icon = "🚨")
            return
        
        for document in self.processor.documents:
            self.page_contents.append(document.page_content)
        
        if len(self.page_contents) != 0:
            st.success(f"Successfully split documents to {len(self.page_contents)} pages!", icon="✅")
        
        text_splitter = CharacterTextSplitter(separator=" ", is_separator_regex=True, chunk_size=50, chunk_overlap=0)
        split_texts = []

        for text in self.page_contents:
            split_texts.extend(text_splitter.split_text(text))
        
        self.db = Chroma.from_texts(split_texts, self.embedding_client)

        if self.db:
            st.success(f"Successfully created Chroma Collection!", icon="✅")
        else:
            st.error("Failed to create Chroma Collection!", icon="🚨")
    
    def query_collection(self, query) -> Document:
        if self.db:
            docs = self.db.similarity_search(query)
            if docs:
                st.write(f"Query Result: {docs[0].page_content}")
                return docs[0]
            else:
                st.error("No matching documents found!", icon = "🚨")
        else:
            st.error("No Chroma Collection created!", icon = "🚨")

if __name__ == "__main__":
    st.title("Chroma Collector")

    model_name = "textembedding-gecko@003"
    project = "YOUR-PROJECT-ID"
    location = "us-central1"
    
    processor = DocumentProcessor()
    processor.ingest_documents()
    embedding_client = EmbeddingClient(model_name, project, location)

    chroma_creator = ChromaCollectionCreator(processor, embedding_client)

    with st.form("Load data to Chroma"):
        st.write("Select PDFs for ingestion then click submit.")
        submitted = st.form_submit_button("Submit")

        if submitted:
            chroma_creator.create_collection()
            chroma_creator.query_collection("Gemini")
