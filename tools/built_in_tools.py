from langchain_community.tools import DuckDuckGoSearchRun, ShellTool

# pip install -U ddgs
search_tool = DuckDuckGoSearchRun()

result = search_tool.invoke('news on iran vs war today?')

# output : 1 hour ago ·Follow NBCNewsfor live updates on the latest about thewarwithIran the energy crisis.

print(result)

# pip install langchain-experimental
shell_tool = ShellTool()

result2 = shell_tool.invoke("ls")

print(result2)

"""
ls
README.md
built_in_tools.py
"""
