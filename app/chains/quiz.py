import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_quiz(retriever):
    docs = retriever.invoke("questions")
    text = " ".join([d.page_content for d in docs[:1]])

    model = genai.GenerativeModel("models/gemini-flash-latest")

    response = model.generate_content(f"""
    Generate 5 quiz questions with answers.

    Content:
    {text}
    """)

    return response.text