import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_revision_plan(retriever):
    docs = retriever.invoke("topics")
    text = " ".join([d.page_content for d in docs])

    model = genai.GenerativeModel("models/gemini-flash-latest")

    response = model.generate_content(f"""
    Create a clear 5-day revision plan with topics and subtopics.

    Content:
    {text}
    """)

    return response.text