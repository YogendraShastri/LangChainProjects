## Models (LangChain) — `models/` folder

This README documents **only** the `models/` folder in this project. It contains small, runnable examples showing how to use:

- **Chat models** (message-in / message-out)
- **LLMs** (string-in / string-out; “traditional” text completion interface)
- **Embedding models** (text → vector)

---

## Folder structure

```text
models/
  ChatModels/
    openai_chat_model.py
    gemini_chat_model.py
    gemini_chat_models_with_roles.py
  LLMS/
    open_ai_llm.py
    llm_gemini.py
  EmbeddingModels/
    gemini_embedding_models.py
```

---

## Concepts in LangChain

### Chat Models

- **Input**: a *list of messages* (or a string, depending on wrapper)
- **Output**: an `AIMessage` (or message-like object)
- **Use when**: you need multi-turn conversation, system instructions, tool/function calling, or structured “messages” context

In LangChain, message types commonly include:

```text
SystemMessage  : sets behavior/persona/instructions
HumanMessage   : user input
AIMessage      : model response (also used as chat history)
ToolMessage    : tool/function call result
```

### LLMs (text completion style)

- **Input**: a single string prompt
- **Output**: a single string completion
- **Use when**: you want a simple string-in/string-out interface, or you’re following older completion-style APIs

### Embeddings

- **Input**: text (string)
- **Output**: a vector (list[float]) used for semantic search, RAG, clustering, similarity, etc.

---

## Prerequisites

### Environment variables

These scripts expect keys in your environment (commonly via a `.env` file):

- **OpenAI**: `OPENAI_API_KEY`
- **Google Gemini**: `GEMINI_API_KEY`

### Python dependencies (high level)

The examples use:

- `python-dotenv` (for `load_dotenv()`)
- `langchain-openai` (OpenAI wrappers)
- `langchain-google-genai` (Gemini wrappers)
- `langchain-core` (message classes)

Install dependencies according to your project’s dependency manager (pip/poetry/uv) and ensure you can import the modules referenced by each script.

---

## What each file does

### Chat models

- **`ChatModels/openai_chat_model.py`**
  - Uses `langchain_openai.ChatOpenAI` with `model="gpt-4.1-mini"` and `temperature=0`
  - Calls `.invoke("...")` and prints `response.content`

- **`ChatModels/gemini_chat_model.py`**
  - Uses `langchain_google_genai.ChatGoogleGenerativeAI` with `model="gemini-2.5-flash"` and `temperature=0`
  - Calls `.invoke("...")` and prints `response.content`

- **`ChatModels/gemini_chat_models_with_roles.py`**
  - Uses `SystemMessage` + `HumanMessage` to demonstrate role-based prompting (“persona” / instruction)
  - Calls `.invoke(messages)` and prints `result.content`

### LLMs

- **`LLMS/open_ai_llm.py`**
  - Uses `langchain_openai.OpenAI` (completion-style interface)
  - Calls `.invoke("...")` and prints the returned string

- **`LLMS/llm_gemini.py`**
  - Uses `langchain_google_genai.GoogleGenerativeAI` (completion-style interface)
  - Calls `.invoke("...")` and prints the returned string

### Embeddings

- **`EmbeddingModels/gemini_embedding_models.py`**
  - Placeholder/stub right now (imports only). Extend this file to create an embeddings instance and call `embed_query` / `embed_documents` depending on the wrapper you choose.

---

## How to run (examples)

From the repo root (so relative imports / `.env` are found), run each file directly:

```bash
python models/ChatModels/openai_chat_model.py
python models/ChatModels/gemini_chat_model.py
python models/ChatModels/gemini_chat_models_with_roles.py

python models/LLMS/open_ai_llm.py
python models/LLMS/llm_gemini.py
```

If your environment variables are not already set in the shell, create a `.env` file in your project root with:

```text
OPENAI_API_KEY=...
GEMINI_API_KEY=...
```

---

## Notes / conventions for this folder

- These files are currently **simple scripts** (not reusable functions/classes). That’s great for learning and quick sanity checks.
- If you later want to reuse them across the project, a common next step is to refactor them into:
  - `get_chat_model(provider=..., model=..., temperature=...)`
  - `get_llm(provider=..., model=..., temperature=...)`
  - `get_embeddings(provider=..., model=...)`

