import streamlit as st 


def main():
    st.set_page_config(page_title="multi pdf chatbot",page_icon=":books:")
    st.header("Chat with multiple pdfs :books:")
    st.text_input("Ask a question about your document")

    with st.sidebar:
        st.subheader("Your Documents")
        st.file_uploader("Upload your pdfs", accept_multiple_files=True)
        if st.button("Process"):
            st.write("working")

if __name__ == '__main__':
    main()