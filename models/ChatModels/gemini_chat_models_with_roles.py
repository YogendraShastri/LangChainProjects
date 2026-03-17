from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

chat = ChatGoogleGenerativeAI(model="gemini-2.0-flash", api_key=api_key)

messages = [
    SystemMessage(content="You are a help full assistant always replay on pirate of the caribbean jack tone"),
    HumanMessage(content="What is the capital of india ?")
]

result = chat.invoke(messages)

print(result.content)