from dotenv import load_dotenv
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

chat_template = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistant"),
        MessagesPlaceholder(variable_name="message_history"),
        ("human", "{query}"),
    ]
)

message_history = []
with open("./prompts/temp_momory.txt", "r") as f:
    for raw in f:
        line = raw.strip()
        if not line:
            continue
        lower = line.lower()
        if lower.startswith("human:"):
            message_history.append(HumanMessage(content=line.split(":", 1)[1].strip()))
        elif lower.startswith("ai:"):
            message_history.append(AIMessage(content=line.split(":", 1)[1].strip()))
        else:
            message_history.append(HumanMessage(content=line))

prompt_value = chat_template.invoke(
    {"message_history": message_history, "query": "what his age now?"}
)

print(prompt_value)
