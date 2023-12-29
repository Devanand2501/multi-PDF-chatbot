# MultiPDF ChatBot

Elevate the way you interact with PDF documents using the MultiPDF ChatBot! This powerful tool turns your PDFs into conversational partners, unlocking a seamless dialogue experience for insightful queries and comprehensive information retrieval.

## Features 🌟

- **PDFs in Dialogue**: Load your PDFs and witness them transform into conversational partners, ready to answer your queries.
- **Text Digestion**: The app breaks down text into manageable chunks, ensuring focused and insightful conversations.
- **Language Understanding**: Leveraging smart language models, the app crafts contextually relevant responses.
- **Semantic Insight**: It matches queries with the most relevant information from the PDFs, delivering meaningful responses.
- **Natural Responses**: The chatbot generates natural, informative responses tailored to your queries.

## How It Works

The MultiPDF ChatBot processes PDFs using various libraries and techniques:

- **Libraries Used**:
  - `PyPDF2` for reading PDF files.
  - `streamlit` for the web interface.
  - `sentence_transformers` for sentence embeddings.
  - `HuggingFace Hub` for language models.
  - `FAISS` for managing embeddings and text retrieval.

The app operates in a series of steps:
1. **PDF Processing**: Upload your PDFs using the web interface.
2. **Text Extraction**: Extracts text from uploaded PDFs.
3. **Text Chunking**: Divides text into manageable chunks for efficient processing.
4. **Embedding Generation**: Generates embeddings for text chunks.
5. **Conversation Establishment**: Sets up a conversational chain for the chatbot.

## Deployment

This project is deployed using Streamlit's cloud hosting, providing an accessible and user-friendly interface for engaging with multiple PDF documents seamlessly.

### Try It Out!

To experience the MultiPDF ChatBot:
1. Clone the repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Add your PDFs and initiate the application with `streamlit run app.py`.
