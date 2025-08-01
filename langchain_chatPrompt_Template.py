from langchain.prompts import ChatPromptTemplate
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv


# Load environment variables
load_dotenv(find_dotenv())

# load api key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")

## Initialize LLM
llm_model = ChatGoogleGenerativeAI(
    model='gemini-1.5-flash-latest',
    google_api_key=API_KEY,
    temperature=0.7
)

template_string = """
convert the user review into little bit polite tone {customer_review} and return only the fine tuned review in {language} language.
"""

# Define the chat prompt template
prompt_template = ChatPromptTemplate.from_template(
    template_string,
)

customer_review = "i dont fucking like this product, it is very bad and useless, no one should buy this product, it is a waste of money"
language = "english"

# Create the chat prompt
chat_prompt = prompt_template.format_messages(
    customer_review=customer_review,
    language=language
)

# Generate the response using the LLM
response = llm_model.invoke(chat_prompt)
# Print the response
print("Response:", response.content if hasattr(response, 'content') else response)

