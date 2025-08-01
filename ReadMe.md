## LangChain

### What is LLM (Large Language Model) ?.
- A Large Language Model (LLM) is a type of Artificial Intelligence (AI) model designed to understand and generate human-like text.
- These models are trained on massive amounts of text data and learn statistical patterns, grammar and reasoning abilities from that data.

### How LLM are Trained?
- **Pretraining (Mostly Unsupervised Learning)**:
  - The model try to derive relationships between words and concepts.
  - This phase is unsupervised because it doesn’t rely on labeled datasets.
- **Fine-Tuning (Supervised or Reinforcement Learning)**:
  - After pretraining, LLMs are fine-tuned on smaller, task-specific datasets.
  - This phase is supervised, using labeled examples to teach the model how to perform specific tasks like translation or classification.
- **Transformer** :
  - Transformer enables the LLM to recognize relationships and connections using a self-attention machanism.
  - Self-attention, allowing the model to weight the importance of different words in a sentence, regardless of their position.

### What is LangChain ?
- Open source framework for building applications that leverage verious LLMs.
- It is particularly useful when you want to build LLM-powered applications that go beyond simple prompt-response tasks
- Langchain also allows you to perform some actions on the given data.
- Langchain focuses on Composition and Modularity, means we have small building blocks that we can use to build upon.
- You can combine building blocks like prompts, chains, tools, memory, and agents to create powerful pipelines.

### How Does it works:
- Langchain takes the documents and transform it into VectorStore (chunk of data).
- Vector embedding, Each chunk of text is converted into a vector (a list of numbers) using an embedding model,
- Vector Representation of the text, as models dont understand text, instead it understand numbers.
- The resulting vectors are stored in a VectorStore (e.g., Chroma, Pinecone).These databases are optimized for vector similarity search, i.e., finding the most relevant chunks based on a user query.
- Query Handling, When a user asks a question, the query is also converted into a vector using the same embedding model.
- The VectorStore finds the nearest (most similar) vectors to the query using techniques like cosine similarity.
- Generates an accurate, context-aware response.

### Use Cases of Langchain
- Data Analysis Assistant
- Flight Booking
- Personal Assistant
- Document Q&A Bot (RAG)
- Codebase Chatbot etc.

### LangChain Building Blocks Components:
- LLM Wrappers
- Prompy Templates
- Indexes
- Chains (Combine Sequences)
- Agents

### langchain Prompt Template:
- PromptTemplate is a utility in LangChain used to construct prompts dynamically by filling in variable placeholders.
- We import ChatPromptTemplate from langchain.prompt to provide variables to the model.

**Snippet**
```python
template_string = """
convert the user review into little bit polite tone {customer_review} and return only the fine tuned review in {language} language.
"""

# Define the chat prompt template
prompt_template = ChatPromptTemplate.from_template(
    template_string,
)

customer_review = "i dont fucking like this product, it is very bad and useless, no one should buy this product, it is a waste of money"
language = "english"

# Create the chat prompt
chat_prompt = prompt_template.format_messages(
    customer_review=customer_review,
    language=language
)
```
- from the above image you can see, like fstring we added the variables [{customer_review},{language}] and than while creating chat prompt we provided the variables value.

**PythonFile** : [langchain_chatPrompt_Template.py](langchain_chatPrompt_Template.py)

### langchain Parser
- structuring and formatting data for further processing downstream.
- Data/Text -> Parser -> Extract and Format -> Desired Format

