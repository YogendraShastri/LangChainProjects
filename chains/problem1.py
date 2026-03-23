"""
Take user query
Classify into:
"billing"
"technical"
"general"
Route to correct handler
Generate response
"""

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal


load_dotenv()

class TextClassify(BaseModel):

    query_class : Literal["billing", "technical", "general"] = Field(description="classify the query into any one of the category")

classification_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

parser = PydanticOutputParser(pydantic_object=TextClassify)

prompt = PromptTemplate(
    template="""You are a classifier.User query: {query} Return ONLY valid JSON.
    {format_instruction}
     """,
    input_variables=['query'],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

prompt_billing = PromptTemplate(
    template="you are assistant to help in billing issue, so reply accordingly on user query {query}",
    input_variables=['query']
)

llm = ChatOpenAI()

prompt_technical= PromptTemplate(
    template="you are assistant to help in technical issue, so reply accordingly on user query {query}",
    input_variables=['query']
)


prompt_general = PromptTemplate(
    template="you are assistant to help in general issue, so reply accordingly on user query {query}",
    input_variables=['query']
)

resoning_chain = prompt | classification_llm | parser # this returns the class

query = """
my phone has some charging issue, even after charging for hours, it says low bettery
"""

result = resoning_chain.invoke({'query' : query})

print(result.query_class)

parser2 = StrOutputParser()

conditional_chain= RunnableBranch(
    (lambda x:x.query_class == "billing", prompt_billing | llm | parser2 ),
              (lambda x:x.query_class == "technical", prompt_technical | llm | parser2 ),
              (lambda x:x.query_class == "general", prompt_general | llm | parser2 ),
    RunnableLambda(lambda x: "could not find sentiment")
)

final = resoning_chain | conditional_chain

result = final.invoke({'query' : query})

print(result)



