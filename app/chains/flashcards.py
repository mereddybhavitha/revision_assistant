import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_flashcards(retriever):
    docs = retriever.invoke("important concepts")
    text = " ".join([d.page_content for d in docs])

    model = genai.GenerativeModel("models/gemini-flash-latest")

    response = model.generate_content(f"""
    Create flashcards in this format:
    Q: ...
    A: ...

    Content:
    {text}
    """)

    return response.text