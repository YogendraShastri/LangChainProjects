from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

chat_template = ChatPromptTemplate(
    [
        ("system", "You are a helpful assistant, expert in particular domain: {domain}"),
        ("human", "Explain this topic in simple terms: {topic}"),
    ]
)

message_history = []

# prompt  = chat_template.invoke({'domain': 'cricket', 'topic' : 'sachin tendulkar'})
llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

while True:
    domain = input("Enter Domain (or 'q' to quit): ").strip()
    if domain.lower() in {"q", "quit", "exit"}:
        break

    topic = input("Enter Topic: ").strip()
    messages = chat_template.format_messages(domain=domain, topic=topic)
    message_history.extend(messages)

    response = llm.invoke(messages)
    print(response.content)

    message_history.append(response)

print(message_history)