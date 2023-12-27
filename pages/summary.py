import openai
import os
import streamlit as st  
from dotenv import load_dotenv
from app import get_text

def main():
    st.set_page_config(
        page_title='Summarizer',
        page_icon=':books:'
    )

    api_key = st.secrets['OPENAI_API_KEY']
    # api_key = os.getenv('OPENAI_API_KEY')
    print(api_key)

    st.header("Summarize Multiple PDFs")
    st.subheader("Your Documents")
    total_pdfs = st.file_uploader("Upload your Documents(PDF only)",accept_multiple_files=True,type=['pdf'])

    if st.button("Process"):
        with st.spinner("Processing"):
            whole_text = get_text(total_pdfs=total_pdfs)
            st.write(whole_text)

if __name__ == '__main__':
    main()