import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from app.services.rag_service import process_pdf
from app.chains.revision_plan import generate_revision_plan
from app.chains.flashcards import generate_flashcards
from app.chains.quiz import generate_quiz

st.title("Exam Revision Assistant")

st.write("App is running...")
uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    retriever = process_pdf("temp.pdf")

    if st.button("Generate Revision Plan"):
        try:
            st.subheader(" Revision Plan")
            st.write(generate_revision_plan(retriever))
        except Exception as e:
            st.error(str(e))

    if st.button("Generate Flashcards"):
        st.subheader(" Flashcards")
        st.write(generate_flashcards(retriever))

    if st.button("Generate Quiz"):
        st.subheader(" Quiz")
        st.write(generate_quiz(retriever))
