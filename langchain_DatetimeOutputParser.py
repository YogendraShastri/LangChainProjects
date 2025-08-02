import os
from langchain.output_parsers import DatetimeOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
from datetime import datetime

# Load environment variables
load_dotenv(find_dotenv())
API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the output parser
output_parser = DatetimeOutputParser()
format_instructions = output_parser.get_format_instructions()

current_date = datetime.now().strftime("%Y-%m-%d")

# Prompt Template
template = """
Today is {current_date}.
Extract the exact date and time from the following message:
"{user_message}"

Respond ONLY in this datetime format: {format_instructions}
Do not include any explanation.
"""

prompt_template = ChatPromptTemplate.from_template(template)

chat_prompt = prompt_template.format_messages(
    user_message="I have a meeting scheduled for next Friday at 3 PM.",
    format_instructions=format_instructions,
    current_date=current_date
)

# Initialize Gemini model
llm_model = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash-latest',
    google_api_key=API_KEY,
    temperature=0  # Less creativity, more deterministic output
)

# Get response
response = llm_model.invoke(chat_prompt)

# Parse it using the output parser
try:
    structured_output = output_parser.parse(response.content)
    print("Extracted Date and Time:")
    print(structured_output)
except Exception as e:
    print("Failed to parse response:", response.content)
    raise e
