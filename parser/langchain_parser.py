from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())
API_KEY = os.getenv("GEMINI_API_KEY")

# 1. Define the expected JSON output schema
class TripPlan(BaseModel):
    leave_time: str = Field(description="Time the person wants to leave")
    places: list[str] = Field(description="List of places they want to visit")
    date: str = Field(description="Date of the trip in YYYY-MM-DD format")

# 2. Create output parser from the Pydantic model
output_parser = PydanticOutputParser(pydantic_object=TripPlan)
format_instructions = output_parser.get_format_instructions()

# 3. Prompt Template
template_string = """
Extract structured trip information from the user message.

User message: "{user_message}"

{format_instructions}
"""

prompt_template = ChatPromptTemplate.from_template(template_string)

# 4. User input
user_message = "I want to leave at 7 AM on August 5th and visit Mysore Palace and Brindavan Gardens."

# 5. Format prompt
chat_prompt = prompt_template.format_messages(
    user_message=user_message,
    format_instructions=format_instructions
)

# 6. Initialize Gemini LLM
llm_model = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash-latest',
    google_api_key=API_KEY,
    temperature=0.5
)

# 7. Invoke model
response = llm_model.invoke(chat_prompt)

# 8. Parse response
structured_output = output_parser.parse(response.content)
print("Structured Trip Plan:")
print(structured_output)

print(type(structured_output))

