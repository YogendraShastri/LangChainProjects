from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

model = ChatOpenAI()
parser = StrOutputParser()

prompt = PromptTemplate(
    template="""you are a helpful assistant, help me write a joke on topic {topic}""",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="""explain the joke : {text}""",
    input_variables=['text']
)

chain = RunnableSequence(prompt, model, parser, prompt2, model, parser)

result = chain.invoke({'topic': 'metro'})

print(result)



