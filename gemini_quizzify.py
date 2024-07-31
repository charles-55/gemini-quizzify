import vertexai
import streamlit as st
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel, Part, Content, ChatSession
from langchain_community.document_loaders import PyPDFLoader
import os

class DocumentProcessor:
    def __init__(self):
        self.documents = []
    
    def ingest_documents(self):
        uploaded_files = st.file_uploader("Upload a PDF file", type="pdf", accept_multiple_files=True)

        if uploaded_files is not None:
            for uploaded_file in uploaded_files:
                temp_file_path = uploaded_file.name

                with open(temp_file_path, "wb") as f:
                    f.write(uploaded_file.getvalue())
                    self.documents = PyPDFLoader(temp_file_path).load()
                
                os.unlink(temp_file_path)
            
            st.write(f"Total pages processed: {len(self.documents)}")

def llm_function(chat, query):
    response = chat.send_message(query)
    output = response.candidates[0].content.parts[0].text

    with st.chat_message("model"):
        st.markdown(output)
    
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })
    st.session_state.messages.append({
        "role": "model",
        "content": output
    })

if __name__ == "__main__":
    project = "YOUR-PROJECT-ID"
    vertexai.init(project = project)

    config = generative_models.GenerationConfig(
        temperature=0.4
    )
    model = GenerativeModel(
        "gemini-pro",
        generation_config=config
    )
    chat = model.start_chat()
    st.title("Gemini Quizzify")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for index, message in enumerate(st.session_state.messages):
        content = Content(
            role = message["role"],
            parts = [ Part.from_text(message["content"]) ]
        )
        
        if index != 0:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        chat.history.append(content)

    if len(st.session_state.messages) == 0:
        initial_prompt = "Introduce yourself as Alfie. You use emojis to be interactive. Always speak like a spy. Ask the user to upload their document(s)."
        llm_function(chat, initial_prompt)

    query = st.chat_input("Explore Gemini...")

    if query:
        with st.chat_message("user"):
            st.markdown(query)
        llm_function(chat, query)

    processor = DocumentProcessor()
    processor.ingest_documents()
