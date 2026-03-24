from langchain_core.tools import tool


@tool
def addition_tool(a: int, b: int) -> int:
    """
    Performs Addition of Two Numbers
    """
    return a + b


result = addition_tool.invoke({'a': 100, 'b': 500})

print(result)
print(addition_tool.args)

"""
600
{'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}
"""

# LLM sees this -
print(addition_tool.args_schema.model_json_schema())
