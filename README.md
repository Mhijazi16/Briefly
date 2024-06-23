# 📜 Briefly

Briefly is an innovative application that allows you to chat with your documents using open-source Large Language Models (LLMs). Upload your PDFs, ask questions, and receive relevant answers in no time!

![Briefly-Brave2024-06-2312-46-19-ezgif com-video-to-gif-converter](https://github.com/Mhijazi16/Briefly/assets/45119497/12e3112b-dc66-4624-97c6-6f689e08981c)

## 🚀 Features

- **Interactive Chat**: Engage in a conversation with your documents.
- **Easy Upload**: Upload multiple PDF files effortlessly.
- **Efficient Processing**: Fast and accurate document processing.
- **Open-Source LLMs**: Powered by open-source language models.

## 🛠️ Installation

To get started with Briefly, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Mhijazi16/Briefly.git
    cd Briefly
    ```

2. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

3. **Run the application**:
    ```sh
    streamlit run Briefly.py
    ```

## 📚 Usage

1. **Upload Documents**: Use the sidebar to upload your PDF documents.
2. **Ask Questions**: Enter your questions in the text input field.
3. **Get Answers**: Receive relevant answers extracted from your documents.

## 📝 Code Overview

Here's a brief overview of the main components of the code:

- **Document Reading**: Uses PyPDF2 to read and extract text from PDF documents.
- **Text Splitting**: Utilizes RecursiveCharacterTextSplitter from Langchain to split text into manageable chunks.
- **Embedding and Retrieval**: Implements OllamaEmbeddingWrapper to embed documents and FAISS for efficient retrieval.
- **Interactive Interface**: Built with Streamlit to provide a user-friendly interface.
