from langchain_openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

model = OpenAI(api_key=api_key, temperature=0)

result = model.invoke("What is the capital of india")

print(result)