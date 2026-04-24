# 🤖 RAG Chatbot

A smart AI chatbot that reads your PDF documents and answers questions about them — built with Python, LangChain, ChromaDB, and GPT-4o-mini.

## 💡 What it does
- Upload any PDF document
- Ask questions about it in plain English
- Get instant AI-powered answers with source references

## 🛠️ Built With
- Python
- LangChain
- ChromaDB
- OpenAI GPT-4o-mini
- HuggingFace Embeddings
- Streamlit

## 🚀 How to Run Locally

### 1. Clone the repository
git clone https://github.com/chandupatel-ai/rag-chatbot.git
cd rag-chatbot

### 2. Create virtual environment
python -m venv venv
venv\Scripts\activate.bat

### 3. Install packages
pip install openai langchain langchain-community chromadb sentence-transformers pypdf streamlit python-dotenv

### 4. Add your OpenAI API key
Create a .env file and add:
OPENAI_API_KEY=your-key-here

### 5. Run the chatbot
streamlit run app.py

## 📁 Project Structure
rag-chatbot/
├── app.py              # Streamlit chat interface
├── ingest.py           # PDF processing and storage
├── rag_pipeline.py     # RAG pipeline and AI responses
├── docs/               # Put your PDFs here
├── .env                # Your API key (never share this)
└── requirements.txt    # Project dependencies

## 🔒 Security
- Never commit your .env file
- Your API key is protected by .gitignore

## 👨‍💻 Author
Chandu - chandupatel-ai
