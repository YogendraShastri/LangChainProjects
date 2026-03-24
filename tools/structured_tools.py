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
