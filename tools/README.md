## What is tools?
A tool is just a python function (or API) that is packaged in a way
the LLM can understand and call when needed.

LLMs (like GPT) are great at : 
- Reasoning 
- Language Generation

But they cant do things like
- Access Live Data
- Do reliable math
- Calls API
- Run Code
- Interact with Database


### Tool Available on LangChain
1. Built-In Tools
2. Custom Tools

### How Tools Fits into Agent EcoSystem ?
An AI Agent is nothing but an LLM-Powered System that can autonomously think. 
decide and take actions using external tools or APIs to achieve a Goal.

### Built-In Tools
A Built-In tools is tool that LangChain already provides for you - its pre-built, production
ready and require minimal setup.

You don't have to write production logic yourself - you just import and use it.

Examples :
- DuckDuckGoSearchRun
- ShellTool
- RequestGetTool
- GmailSendMessageTool
- SlackSendMessageTool

Example:
```python
from langchain_community.tools import DuckDuckGoSearchRun

# pip install -U ddgs
search_tool = DuckDuckGoSearchRun()

result = search_tool.invoke('news on iran vs war today?')

print(result)
```

### Custom Tools
As name suggests, A custom tool is a tool that you define yourself.

Use Them When
- you want to call your own API.
- You want to encapsulate business logic.
- You want the LLM to interact with your database, product or app.

```python
from langchain_core.tools import tool


@tool
def addition_tool(a: int, b: int) -> int:
    """
    Performs Addition of Two Numbers
    """
    return a + b

result = addition_tool.invoke({'a': 100, 'b': 500})

print(result)
```

### Way to Create Tools
1. Using @tool Decorator - example shown above.
2. Using StructuredTool & Pydantic
3. Using BaseTool Class

### StructuredTool & Pydantic
A Structured Tool in LangChain is a Special type of tool where the input to the tool
follows a structured schema, typically defined using a pydantic model.

```python
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field


class AdditionSchema(BaseModel):
    a : int = Field(..., description="the first number to add")
    b : int = Field(..., description="the second number to add")


def addition_tool(a: int, b: int) -> int:
    return a + b

# actual initialization
addition_tool_init = StructuredTool.from_function(
    func=addition_tool,
    name="addition_tool",
    description="add two numbers together",
    args_schema=AdditionSchema
)

result = addition_tool_init.invoke({'a' : 10, 'b': 20})

print(result)
```

### BaseTool 
Base Tool is the abstract base class for all tools in LangChain.
if defines the core structure and interface that any tool must follow,
whether its simple one-liner or fully customized function.

```python
from langchain_core.tools import BaseTool
from typing import Type
from  pydantic import BaseModel, Field


class AdditionSchema(BaseModel):
    a : int = Field(..., description="the first number to add")
    b : int = Field(..., description="the second number to add")

class AdditionTool(BaseTool):
    name : str = "addition tool"
    description : str = "add two numbers"
    args_schema : Type[BaseModel] = AdditionSchema

    def _run(self, a: int, b: int) -> int:
        return a + b

add_tool = AdditionTool()

result = add_tool.invoke({'a': 10, 'b': 20})

print(result)
```

- you can make async version of your tools
- customization is better




