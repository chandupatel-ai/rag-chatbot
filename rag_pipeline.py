from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

CHROMA_DIR = "chroma_db"

def answer_question(question):
    try:
        embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        vectordb = Chroma(
            persist_directory=CHROMA_DIR,
            embedding_function=embeddings
        )

        docs = vectordb.similarity_search(question, k=3)

        if not docs:
            return "No relevant documents found.", []

        context = "\n\n".join([d.page_content for d in docs])

        answer = f"Answer based on documents:\n\n{context[:500]}..."

        sources = [d.metadata.get("source", "unknown") for d in docs]

        return answer, sources

    except Exception as e:
        return f"Error: {str(e)}", []