from langchain.prompts import ChatPromptTemplate
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.output_parsers import CommaSeparatedListOutputParser
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Load API Key
API_KEY = os.getenv("GEMINI_API_KEY")

# Parser for comma-separated lists
output_parser = CommaSeparatedListOutputParser()

# Format instructions for the parser
format_instructions = output_parser.get_format_instructions()

template = """
Give the Top 5 Tourist Attraction in the city {city}.
{format_instructions}
 """

prompt_template = ChatPromptTemplate.from_template(template)

# Create the chat prompt
chat_prompt = prompt_template.format_messages(
    city="Bangalore",
    format_instructions=format_instructions
)

# initialize the LLM
llm_model = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash-latest',
    google_api_key=API_KEY,
    temperature=0.7
)

# generate the response using the LLM
response = llm_model.invoke(chat_prompt)

# Parse the response using the output parser
structured_output = output_parser.parse(response.content)
print("Top 5 Tourist Attractions in Bangalore:")
for place in structured_output:
    print(f"- {place}")





