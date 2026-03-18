## Structured Output (LangChain) — `structured_output/` folder

**Structured output** means: instead of returning free-form text, the model returns data that matches a schema, for example:

```text
{ "summary": "...", "sentiment": "negative" }
```

In LangChain, the easiest way is:

- `chat_model.with_structured_output(schema)`

Where `schema` can be a **Pydantic model** or a **JSON Schema dict**.

---

## What’s inside this folder

```text
structured_output/
  README.md
  structured_output_langchain.py
  structured_output_json_langchain.py
```

- **`structured_output_langchain.py`**: structured output using a **Pydantic** schema.
- **`structured_output_json_langchain.py`**: structured output using a **JSON Schema** dict.

---

## Two “types” of models (practical view)

### 1) Models that support structured output in LangChain

These are typically **chat models** that can follow a schema and that LangChain integrations implement `with_structured_output` for.

- In this repo we use: `langchain_openai.ChatOpenAI`
- (Gemini / other providers can also support structured outputs depending on integration + model)

If you try this on a model wrapper that does not implement it (example: `langchain_openai.OpenAI` completion-style),
you can hit `NotImplementedError`.

### 2) Models (or wrappers) that don’t support it

For those, you usually do:

- Ask the model to output JSON in the prompt
- Then parse/validate using **output parsers** (e.g., PydanticOutputParser / JsonOutputParser)

---

## Example 1: Pydantic schema (recommended)

File: `structured_output_langchain.py`

- Define a schema:
  - `class Review(BaseModel): summary: str, sentiment: str`
- Call:
  - `structured_output_model = model.with_structured_output(Review)`
- Invoke and get back a parsed object.

---

## Example 2: JSON Schema dict

File: `structured_output_json_langchain.py`

Important: LangChain expects a **valid JSON schema** with top-level fields like:

- `title`
- `description`
- `type: "object"`
- `properties: {...}`
- `required: [...]`

---

## How to run

From the repo root:

```bash
python structured_output/structured_output_langchain.py
python structured_output/structured_output_json_langchain.py
```

### Environment variables

These examples use OpenAI chat API:

- `OPENAI_API_KEY`

---