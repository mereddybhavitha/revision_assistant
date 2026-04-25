from app.loaders.pdf_loader import load_pdf
from app.rag.splitter import split_docs
from app.rag.vector_store import create_vector_store
from app.rag.retriever import get_retriever

def process_pdf(file_path):
    docs = load_pdf(file_path)
    chunks = split_docs(docs)
    db = create_vector_store(chunks)
    return get_retriever(db)