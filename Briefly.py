import streamlit as st 
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

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
    st.set_page_config(page_icon=":scroll:",page_title="Briefly")
    st.header("Chat With Your Documents :scroll:")
    input = st.text_input("Enter Question !")

    with st.sidebar: 
        st.subheader("Upload Your Documents")
        documents = st.file_uploader("upload your files here", accept_multiple_files=True)
        if st.button(":package: Process") : 
            raw_text  = read_docs(documents)
            chunks= split_text(raw_text)
            st.write(chunks)


if __name__ == "__main__": 
    main()