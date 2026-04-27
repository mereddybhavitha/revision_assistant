import streamlit as st
from app.services.rag_service import process_pdf
from app.chains.revision_plan import generate_revision_plan
from app.chains.flashcards import generate_flashcards
from app.chains.quiz import generate_quiz

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Exam Assistant", layout="wide")

# ---------------- CUSTOM STYLE ----------------
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}
.card {
    padding: 20px;
    border-radius: 15px;
    background: white;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-top: 10px;
}
h1 {
    color: #2c3e50;
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
st.sidebar.title(" Exam Revision Assistant")
st.sidebar.markdown("Upload your PDF and generate smart study materials.")

uploaded_file = st.sidebar.file_uploader(" Upload PDF", type="pdf")

# ---------------- HEADER ----------------
st.title(" Smart Study Dashboard")
st.markdown("Generate **Revision Plans, Flashcards, and Quizzes** instantly using AI.")

# ---------------- MAIN LOGIC ----------------
if uploaded_file:

    # Save uploaded file
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    st.success(" PDF uploaded successfully!")

    # Process PDF
    retriever = process_pdf("temp.pdf")

    # Tabs UI
    tab1, tab2, tab3 = st.tabs([" Revision Plan", " Flashcards", " Quiz"])

    # ---------------- REVISION ----------------
    with tab1:
        if st.button("Generate Revision Plan"):
            with st.spinner("Generating revision plan..."):
                result = generate_revision_plan(retriever)

                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader(" Revision Plan")
                st.write(result)

                st.download_button(
                    "⬇ Download",
                    data=result,
                    file_name="revision_plan.txt"
                )
                st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- FLASHCARDS ----------------
    with tab2:
        if st.button("Generate Flashcards"):
            with st.spinner("Generating flashcards..."):
                result = generate_flashcards(retriever)

                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader(" Flashcards")
                st.write(result)

                st.download_button(
                    "⬇ Download",
                    data=result,
                    file_name="flashcards.txt"
                )
                st.markdown('</div>', unsafe_allow_html=True)

    # ---------------- QUIZ ----------------
    with tab3:
        if st.button("Generate Quiz"):
            with st.spinner("Generating quiz..."):
                result = generate_quiz(retriever)

                st.markdown('<div class="card">', unsafe_allow_html=True)
                st.subheader(" Quiz")
                st.write(result)

                st.download_button(
                    "⬇ Download",
                    data=result,
                    file_name="quiz.txt"
                )
                st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info(" Please upload a PDF from the sidebar to begin.")

# ---------------- FOOTER ----------------
st.markdown("---")
