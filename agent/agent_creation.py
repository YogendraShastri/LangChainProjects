from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
from langchain.agents import create_agent

load_dotenv()

search_tool = DuckDuckGoSearchRun()
@tool
def get_user_credentials():
    """Fetch random username and password (for testing)"""
    try:
        url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
        response = requests.get(url, timeout=5)
        response.raise_for_status()

        data = response.json()
        return {
            "username": data["data"]["login"]["username"],
            "password": data["data"]["login"]["password"]
        }
    except Exception as e:
        return {"error": str(e)}


agent = create_agent(
    model="gpt-4.1",
    tools=[search_tool, get_user_credentials],
    system_prompt="You are a helpful assistant. Be concise and accurate."
)

messages = [
    HumanMessage(content="What is the latest news about war between US and Iran?")
]

result = agent.invoke({
    "messages": messages
})

print(result["messages"][-1].content)