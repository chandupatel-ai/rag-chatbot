import streamlit as st
import os

st.title("My RAG Chatbot")

# Sidebar
with st.sidebar:
    st.header("Upload Documents")

    uploaded = st.file_uploader(
        "Upload PDFs", type="pdf", accept_multiple_files=True
    )

    if uploaded:
        if st.button("Ingest Documents"):

            from ingest import ingest_documents

            os.makedirs("docs", exist_ok=True)

            for f in uploaded:
                with open(os.path.join("docs", f.name), "wb") as out:
                    out.write(f.read())

            with st.spinner("Processing..."):
                ingest_documents()

            st.success("Documents processed!")

# Main area
question = st.text_input("Ask a question")

if question:
    from rag_pipeline import answer_question

    answer, sources = answer_question(question)

    st.write("Answer:", answer)

    if sources:
        for s in sources:
            st.write(s)