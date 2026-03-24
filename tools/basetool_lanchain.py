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