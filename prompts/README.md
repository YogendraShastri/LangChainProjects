## Prompts (LangChain) — `prompts/` folder

This README documents **only** the `prompts/` folder in this project. It contains small examples of how to create and use **prompt templates** in LangChain.

- **Prompts** are the input instructions given to a model to guide its output.

---

## What’s inside this folder

```text
prompts/
  README.md
  langchain_prompt_template.py
  langchain_prompt_template_user_input.py
  langchain_ChatPromptTemplate.py
  langchain_chatPrompt_Template.py
  langchain_message_placeholder.py
  prompt_generator.py
  template.json
  temp_momory.txt
```

- **`langchain_prompt_template.py`**: basic `PromptTemplate` (single-turn, string prompt).
- **`langchain_prompt_template_user_input.py`**: takes user input + loads a prompt from `template.json`, then runs it.
- **`prompt_generator.py`**: creates a `PromptTemplate` and saves it to `template.json`.
- **`langchain_ChatPromptTemplate.py`**: `ChatPromptTemplate` + `ChatOpenAI` with interactive user input.
- **`langchain_chatPrompt_Template.py`**: `ChatPromptTemplate` with **Gemini** (`ChatGoogleGenerativeAI`) example.
- **`langchain_message_placeholder.py`**: `MessagesPlaceholder` to inject message history.
- **`temp_momory.txt`**: simple history store used by `langchain_message_placeholder.py`.

---

## Ways of prompt writing (prompting strategies)

1. **Zero-shot prompting**: ask directly without examples.
2. **Few-shot prompting**: provide a few examples, then ask.
3. **Chain-of-thought (CoT)**: encourage step-by-step reasoning (use carefully; often you want “concise reasoning” instead of exposing full chain).
4. **Tree-of-thoughts (ToT)**: explore multiple reasoning branches before deciding.

---

## Types of prompts

- **Static prompt**: fixed text, always the same instructions.
- **Dynamic prompt**: uses a template + variables, filled at runtime.

### Dynamic prompt example

```text
You are a helpful assistant.
Write an introduction about the topic: {topic}
Constraints:
- Exactly {lines} lines
```

Then you pass values for `topic` and `lines` at runtime.

---

## PromptTemplate (single-turn, string-in / string-out)

Use `PromptTemplate` when your model expects a **single string prompt** (classic “completion” style).

Your example scripts:

- `langchain_prompt_template.py`
- `langchain_prompt_template_user_input.py` (loads the template from `template.json`)

---

## ChatPromptTemplate (multi-turn, list of messages)

Use `ChatPromptTemplate` for chat models. It builds a **list of messages** such as `system` + `human` + `ai`.

Your example scripts:

- `langchain_ChatPromptTemplate.py` (OpenAI chat)
- `langchain_chatPrompt_Template.py` (Gemini chat)

---

## PromptTemplate vs ChatPromptTemplate (quick compare)

- **PromptTemplate**
  - **Output**: a formatted string prompt
  - **Best for**: simple single-turn prompts; older completion-style LLM wrappers

- **ChatPromptTemplate**
  - **Output**: message objects (system/human/ai/tool)
  - **Best for**: modern chat models, multi-turn conversations, structured message context

---

## Roles in chat prompts

Typical roles you’ll use:

- **system**: sets behavior/persona/instructions
- **human**: user input
- **ai**: model output (also used for storing history)
- **tool**: tool/function call results (when using tool calling)

---

## Message history (chat memory)

A simple “history” is usually a list like:

```python
messages = [
  # SystemMessage(...)
  # HumanMessage(...)
  # AIMessage(...)
]
```

---

## MessagesPlaceholder (inject history into a template)

Use `MessagesPlaceholder` when you want your template to include prior messages.

In this folder:

- `langchain_message_placeholder.py` loads `temp_momory.txt` and injects it into the template via:
  - `MessagesPlaceholder(variable_name="message_history")`

### Recommended `temp_momory.txt` format

```text
human: who is narendra modi
ai: narendra modi is prime minister of india
```

---

## How to run

From the repo root:

```bash
python prompts/langchain_prompt_template.py
python prompts/langchain_prompt_template_user_input.py
python prompts/langchain_ChatPromptTemplate.py
python prompts/langchain_chatPrompt_Template.py
python prompts/langchain_message_placeholder.py
```

### Environment variables

- **OpenAI** examples need: `OPENAI_API_KEY`
- **Gemini** examples need: `GEMINI_API_KEY`

