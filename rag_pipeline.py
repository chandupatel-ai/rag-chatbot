import os
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

load_dotenv()
CHROMA_PATH = "chroma_db"

def get_answer(question):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
    docs = db.similarity_search(question, k=3)
    context = "\n\n".join([doc.page_content for doc in docs])
    llm = ChatGroq(model="llama3-8b-8192", temperature=0, api_key=os.getenv("GROQ_API_KEY"))
    prompt = f"Answer based on this context:\n\n{context}\n\nQuestion: {question}"
    response = llm.invoke([HumanMessage(content=prompt)])
    return response.content