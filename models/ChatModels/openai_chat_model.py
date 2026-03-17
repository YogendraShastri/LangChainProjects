import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load variables from .env file
load_dotenv()

# Access the API key using os.getenv()
api_key = os.getenv("OPENAI_API_KEY")
llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0, api_key=api_key)

# temperature - randomness towards 0 - more deterministic, and towards 2 more randomness
# also if temperature is 0 all the time u get the same answer but if increase randomness different ans each time

# Invoke model
response = llm.invoke("What is the capital of india")
print(response.content)