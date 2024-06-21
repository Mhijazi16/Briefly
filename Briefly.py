import streamlit as st 
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import ollama
from langchain.vectorstores import FAISS
from langchain_community.llms import Ollama

model = Ollama(model="llama3")
class OllamaEmbeddingWrapper:
    def __init__(self, model_name):
        self.model_name = model_name

    def embed_documents(self, texts):
        return [ollama.embeddings(model=self.model_name, prompt=text)['embedding'] for text in texts]
    def __call__(self, text):
        return ollama.embeddings(model=self.model_name, prompt=text)['embedding']

def get_retriever(chunks): 
    embedding_model = OllamaEmbeddingWrapper(model_name="nomic-embed-text")
    return FAISS.from_texts(texts=chunks,embedding=embedding_model).as_retriever()

def handle_questions(question): 
    with st.spinner("Retrieving relevent information"): 
        context = st.session_state.retriever.invoke(question)
    with st.spinner("generating"): 
        st.write_stream(
            model.stream(f"Question: {question} \n\n Context: {context}"))

def split_text(raw_text):
    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "],
        chunk_size=500,
        chunk_overlap=200,
        length_function=len
    )
    return splitter.split_text(raw_text)

def read_docs(documents): 
    text = ""
    for doc in documents : 
        file = PdfReader(doc)
        for page in file.pages: 
            text += page.extract_text()
    return text

def main(): 
    if "retriever" not in st.session_state: 
        st.session_state.retriever = None

    st.set_page_config(page_icon=":scroll:",page_title="Briefly")
    st.header("Chat With Your Documents :scroll:")

    question = st.text_input("Enter Question !")
    if question: 
        handle_questions(question)

    with st.sidebar: 
        st.subheader("Upload Your Documents")
        documents = st.file_uploader("upload your files here", accept_multiple_files=True)
        if st.button(":package: Process") : 
            with st.spinner("Processing") : 
                raw_text  = read_docs(documents)
                chunks = split_text(raw_text)
                st.session_state.retriever = get_retriever(chunks)

if __name__ == "__main__": 
    main()