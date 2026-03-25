from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import requests
import json

messages = []
load_dotenv()

@tool
def get_user():
    """ tool to fetch username, password for testing using api call on database"""
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    response_json = json.loads(response.content)
    user_name = response_json['data']['login']['username']
    password = response_json['data']['login']['password']
    return {
        'username' : user_name,
        'password' : password
    }

model = ChatOpenAI()

# tool binding
model_with_tool = model.bind_tools([get_user])

prompt = HumanMessage("fetch username password from database for testing")
messages.append(prompt)

result = model_with_tool.invoke(messages) # tool calling
messages.append(result)
# print(result)

"""
content='' additional_kwargs={'tool_calls': [{'id': 'call_pWk3rwiYp19pJvDZZICcZE5o', 'function': {'arguments': '{}', 'name': 'get_user'}, 'type': 'function'}], 'refusal': None} response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 53, 'total_tokens': 63, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-DMzY9PFaSgWKOOwhC6qcZEaw9zjYc', 'service_tier': 'default', 'finish_reason': 'tool_calls', 'logprobs': None} id='lc_run--019d20d2-e108-7c60-b4cc-276fcd01e368-0' tool_calls=[{'name': 'get_user', 'args': {}, 'id': 'call_pWk3rwiYp19pJvDZZICcZE5o', 'type': 'tool_call'}] invalid_tool_calls=[] usage_metadata={'input_tokens': 53, 'output_tokens': 10, 'total_tokens': 63, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
"""

tool_resp = get_user.invoke(result.tool_calls[0])
messages.append(tool_resp)

#print(tool_resp)
"""
ToolMessage
content='{"username": "greenladybug792", "password": "compass"}' name='get_user' tool_call_id='call_BpOzZZAy7FSuFJyYZFSNetWi'

we can return this tool message to LLM and get response
"""

final_llm_response = model.invoke(messages)

print(final_llm_response.content)

# The username is ticklishpeacock647 and the password is julian.