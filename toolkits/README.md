### Toolkits

A toolkit is just a collection or bundle of related tools that serve
a common purpose packaged together for convenience and reusability.


in LangChain: 
- A toolkit might be : GoogleDriveToolKit 
- and it can contain the following tools

GoogleDriveCreateFile
GoogleDriveSearchFile
GoogleDriveReadFile
etc...


```python
from langchain_core.tools import tool

@tool
def add_values(a: int, b : int) -> int:
    """add two values"""
    return a + b

@tool
def sub_values(a: int, b : int) -> int:
    """substract two values"""
    return a - b

@tool
def mul_values(a: int, b : int) -> int:
    """multipy two values"""
    return a * b

class MathToolkit:
    def get_tools(self):
        return [add_values, sub_values, mul_values]

tool_kit = MathToolkit()
all_tools = tool_kit.get_tools()

for tool in all_tools:
    print(tool.name, "->", tool.description)

"""
add_values -> add two values
sub_values -> substract two values
mul_values -> multipy two values
"""
```

### Tool Binding

Tool binding is the step where you register your tools with a Language Model so that :
1. The LLM knows what tools are available
2. The LLM knows what each tool does (via description)
3. The LLM knows what input format to use (via schema)

Example: 

```
model = ChatOpenAI()

# tool binding
model_with_tool = model.bind_tools([tool1_name, tool2_name])
```

### Tool Calling

Tool calling is the process where the LLM (language model) decides, during a conversation or task,
that it needs to use a specific tool (function) and generate structured output with:
- the name of the tool
- and the arguments to call it with.

~ The LLM does not actually run the tool - it just suggest tbe tool and input arguments,
The actual execution is handled by LangChain or you.


```python
model = ChatOpenAI()

# tool binding
model_with_tool = model.bind_tools([get_user])

prompt = "fetch username password from database for testing"

result = model_with_tool.invoke(prompt)

print(result)

"""
content='' additional_kwargs={
'tool_calls': [{'id': 'call_pWk3rwiYp19pJvDZZICcZE5o', 'function': {'arguments': '{}', 'name': 'get_user'}, 'type': 'function'}], 'refusal': None} response_metadata={'token_usage': {'completion_tokens': 10, 'prompt_tokens': 53, 'total_tokens': 63, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-DMzY9PFaSgWKOOwhC6qcZEaw9zjYc', 'service_tier': 'default', 'finish_reason': 'tool_calls', 'logprobs': None} id='lc_run--019d20d2-e108-7c60-b4cc-276fcd01e368-0' 
tool_calls=[{'name': 'get_user', 'args': {}, 'id': 'call_pWk3rwiYp19pJvDZZICcZE5o', 'type': 'tool_call'}] invalid_tool_calls=[] usage_metadata={'input_tokens': 53, 'output_tokens': 10, 'total_tokens': 63, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
"""
```

### Tool Execution

Tool Execution is the step where the actual python function (tool) is run
using the input arguments that the LLM suggested during tool calling.

- Tool Execution is when u or LangChain actually run
- and get result 





