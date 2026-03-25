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



