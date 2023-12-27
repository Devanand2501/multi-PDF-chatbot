import streamlit as st 
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings,HuggingFaceInstructEmbeddings
from sentence_transformers import SentenceTransformer
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.llms import HuggingFaceHub
from langchain.chains import ConversationalRetrievalChain
from html_template import css, user_template, bot_template


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
    # embeddings = OpenAIEmbeddings() 
    embeddings = HuggingFaceInstructEmbeddings(model_name="sentence-transformers/quora-distilbert-base",
    encode_kwargs = {'normalize_embeddings': True})
    # model = SentenceTransformer('all-MiniLM-L6-v2')
    # embeddings = model.encode(chunks)
    vectorStore = FAISS.from_texts(texts=chunks,embedding=embeddings)
    return vectorStore

def get_conversationChain(vectorStore):
    llm = ChatOpenAI()
    # llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature":0.5, "max_length":512})
    memory = ConversationBufferMemory(memory_key='chat_history',return_messages=True)
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        memory=memory,
        retriever=vectorStore.as_retriever()
        )
    return chain

def handle_userQuestion(question):
    response = st.session_state.conversation({'question': question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)

def main():
    load_dotenv()
    st.set_page_config(page_title="multi pdf chatbot",page_icon=":books:")
    st.write(css, unsafe_allow_html=True)
    st.header("Chat with multiple pdfs :books:")
    user_question = st.text_input("Ask a question about your document")

    if user_question:
        handle_userQuestion(user_question)
    if "conversation" not in st.session_state:
        st.session_state.conversation = None 
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None


    st.write(user_template.replace("{{MSG}}","HELLO ROBOT"),unsafe_allow_html=True)
    st.write(bot_template.replace("{{MSG}}","HELLO HUMAN"),unsafe_allow_html=True)


    with st.sidebar:
        st.subheader("Your Documents")
        total_pdfs = st.file_uploader("Upload your pdfs", accept_multiple_files=True,type=['pdf'])
        if st.button("Process"):
            with st.spinner("Processing"):
                # get the whole text
                raw_text = get_text(total_pdfs=total_pdfs)

                # get the chuncks of text
                chunk_text = get_chunks(raw_text)

                # create a vector store i.e. FIASS used which is used to store the embeddings locally
                vector_store = get_vectorStore(chunk_text)

                st.session_state.conversation = get_conversationChain (vector_store)
            st.write("PROCESSING HOGAYA JI")

if __name__ == '__main__':
    main()