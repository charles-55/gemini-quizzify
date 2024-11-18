import streamlit as st
import vertexai
from vertexai.preview import generative_models
from vertexai.preview.generative_models import GenerativeModel

from document_processor import DocumentProcessor
from embedding_client import EmbeddingClient
from chroma_creator import ChromaCollectionCreator

class QuizGenerator:
    def __init__(self, topic = None, num_questions = 1, vectorstore = None):
        if not topic:
            self.topic = "General Knowledge"
        else:
            self.topic = topic
        
        if num_questions > 10:
            raise ValueError("Number of questions can not be greater than 10!")
        self.num_questions = num_questions

        self.vectorstore = vectorstore
        self.llm_model = None
        self.template = """
            You are an expert at the topic: {self.topic}

            Follow the instructions below and create a quiz:
            1. Generate a question based on the topic provided and context as key "question"
            2. Provide 4 multiple choice answers to the question as a list of key-value pairs "choices"
            3. Provide the correct answer for the question from the list of answers as key "answer"
            4. Provide an explanation as to why the answer is correct as key "explanation"

            You must respond as a JSON object with the following structure:
            {{
                "question": "<question>",
                "choices": [
                    {{"key": "A", "value": "<choice>"}},
                    {{"key": "B", "value": "<choice>"}},
                    {{"key": "C", “value": "<choice>"}},
                    {{"key": "D", "value": "<choice>"}}
                ],
                "answer": "<answer key from choices list>",
                "explanation": "<explanation as to why the answer is correct>"
            }}

            Context: {context}
            """

    def init_llm(self):
        config = generative_models.GenerationConfig(
            temperature = 0.4,
            max_output_tokens = 400
        )
        self.llm_model = GenerativeModel(
            "gemini-pro",
            generation_config = config
        )

    def generate_question_with_vectorstore(self):
        if self.llm_model is not None:
            print("LLM is initialized and available")
        else:
            print("LLM is not initialized")

        if self.vectorstore is not None:
            print("Vectorstore is initialized and available")
        else:
            print("Vectorstore is not initialized")
    
    def retrieve_context_from_vectorstore(self, quiz_topic):
        relevant_documents = self.vectorstore.search(quiz_topic)
        self.relevant_context = process_documents(relevant_documents)

if __name__ == "__main__":
    st.title("Quizzify")

    model_name = "textembedding-gecko@003"
    project = "gemini-quizify-430217"
    location = "us-central1"
    
    processor = DocumentProcessor()
    processor.ingest_documents()
    embedding_client = EmbeddingClient(model_name, project, location)
    chroma_creator = ChromaCollectionCreator(processor, embedding_client)

    generated = False
    question = None

    with st.form("quiz_generator"):
        st.subheader("Quiz Generator")
        st.write("Select PDFs for ingestion, enter a quiz topic, and select the number of questions you want.")
        topic = st.text_input("Topic for Quiz")
        amount = st.slider("How many questions would you like?", 1, 20)
        generator_submitted = st.form_submit_button("Generate and Query")
        
        if generator_submitted:
            chroma_creator.create_collection()
            generated = True
    
    if generated:
        st.subheader(topic)

    question = chroma_creator.generate_question_with_vectorstore(topic, amount)
