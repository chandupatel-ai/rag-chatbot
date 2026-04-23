import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

DOCS_DIR = "docs"
CHROMA_DIR = "chroma_db"

def ingest_documents():
    docs = []

    if not os.path.exists(DOCS_DIR):
        print("Docs folder not found")
        return

    for fname in os.listdir(DOCS_DIR):
        if fname.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DOCS_DIR, fname))
            docs.extend(loader.load())

    if not docs:
        print("No documents found")
        return

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory=CHROMA_DIR
    )

    vectordb.persist()

    print(f"Done! Ingested {len(chunks)} chunks.")