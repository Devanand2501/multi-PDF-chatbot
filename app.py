import streamlit as st 
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def get_text(total_pdfs):
    text = ""
    for pdf in total_pdfs:
        pdf_reader= PdfReader(pdf)
        for pages in pdf_reader.pages:
            text += pages.extract_text()
    return text

def get_chunks(text):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    chunks = splitter.split_text(text)
    return chunks

def get_vectorStore(chunks):
    embeddings = OpenAIEmbeddings() #"gpt-j-6B"
    vectorStore = FAISS.from_texts(text=chunks,embeddings=embeddings)
    return vectorStore

def main():
    load_dotenv()
    st.set_page_config(page_title="multi pdf chatbot",page_icon=":books:")
    st.header("Chat with multiple pdfs :books:")
    st.text_input("Ask a question about your document")

    with st.sidebar:
        st.subheader("Your Documents")
        total_pdfs = st.file_uploader("Upload your pdfs", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get the whole text
                raw_text = get_text(total_pdfs=total_pdfs)

                # get the chuncks of text
                chunk_text = get_chunks(raw_text)

                # create a vector store i.e. FIASS used which is used to store the embeddings locally
                vector_store = get_vectorStore(chunk_text)

if __name__ == '__main__':
    main()