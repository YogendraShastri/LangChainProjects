import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

prompt = PromptTemplate(
    template=(
        "You are a helpful assistant."
        "Write an introduction about the topic: {topic}\n"
        "Constraints:\n"
        "- Exactly {lines} lines\n"
        "- Clear and beginner-friendly\n"
    ),
    input_variables=["topic", "lines"],
)

llm = OpenAI(api_key=api_key, temperature=0)

chain = prompt | llm
result = chain.invoke({"topic": "LangChain", "lines": 5})
print(result)