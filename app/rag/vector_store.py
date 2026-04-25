from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os
print("API KEY:", os.getenv("GOOGLE_API_KEY"))
load_dotenv()

def create_vector_store(docs):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001",
google_api_key="AIzaSyATGueEsfB8vaKhVc1R6YsCCkFyk_u0e1Y"    )

    db = Chroma.from_documents(docs, embeddings)
    return db