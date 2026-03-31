## LangChain Expression Language
- It's LangChain's way of building chains using the | pipe operator — the same symbol you use in Unix terminals. Every component (prompt, LLM, retriever, parser, function) becomes a Runnable, and you chain them together with pipe "|". 
- The output of each step flows automatically as input to the next.
- Chains built with LCEL automatically support advanced execution modes without code changes.




### Why does it exist? 
- Before LCEL, you had to manually call each step, handle output formatting yourself, and write separate code for streaming vs. non-streaming. 
- LCEL gives you streaming, async, batching, and parallel execution for free just by composing with |.

### Example:
```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template("Tell me a fact about {topic}")
llm    = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()

chain = prompt | llm | parser

chain.invoke({"topic": "black holes"})
```

### Runnable
- A Runnable is a standardized interface in LangChain that represents a single unit of work. 
- Many core LangChain components, such as prompt templates, language models (LLMs), output parsers, and retrievers, implement this interface.
- The key characteristic is that all runnables share a common set of execution methods, which allows them to be easily chained together.

#### Common methods like:
1. invoke()
2. batch()
3. stream()
4. etc.
