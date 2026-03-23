from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

llm1 = ChatOpenAI(temperature=0)

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}, also add 1-2 wrong facts as well for testing',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='here is the generated facts tell me how many of facts are true, facts : {text}, example : 3/5',
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt | llm1 | parser | prompt2 | llm1 | parser

result = chain.invoke({'topic' : 'indian railway'})

print(result)

chain.get_graph().print_ascii()

"""
     +-------------+       
     | PromptInput |       
     +-------------+       
            *              
            *              
            *              
    +----------------+     
    | PromptTemplate |     
    +----------------+     
            *              
            *              
            *              
      +------------+       
      | ChatOpenAI |       
      +------------+       
            *              
            *              
            *              
   +-----------------+     
   | StrOutputParser |     
   +-----------------+     
            *              
            *              
            *              
+-----------------------+  
| StrOutputParserOutput |  
+-----------------------+  
            *              
            *              
            *              
    +----------------+     
    | PromptTemplate |     
    +----------------+     
            *              
            *              
            *              
      +------------+       
      | ChatOpenAI |       
      +------------+       
            *              
            *              
            *              
   +-----------------+     
   | StrOutputParser |     
   +-----------------+     
            *              
            *              
            *              
+-----------------------+  
| StrOutputParserOutput |  
+-----------------------+ 
"""