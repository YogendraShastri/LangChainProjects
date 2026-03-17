from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

# load api key
api_key = os.getenv("GEMINI_API_KEY")

# Initialize as a standard LLM
llm = GoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=api_key
)

# Use .invoke() with a string directly
response = llm.invoke("what is the capital of india")
print(response)