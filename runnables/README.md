# LangChain Runnables - Complete Guide

This repository demonstrates the power of **LangChain Runnables**, the modern abstraction for building composable AI pipelines.

---

## What are Runnables?

A **Runnable** is a standard interface in LangChain for any unit that:
- Takes input
- Processes it
- Returns output

Think:
Input → Runnable → Output

---

## Why Runnables?

- Unified interface across components
- Easy composition using `|`
- Supports async, batch, and streaming
- Replaces old Chains

---

## Project Files Overview

- runnable_lambda.py → Function wrapper
- runnable_sequence.py → Sequential pipeline
- runnable_parallel.py → Parallel execution
- runnable_branch.py → Conditional routing
- runnable_passthrough.py → Data passthrough

---

## RunnableLambda

```python
from langchain_core.runnables import RunnableLambda

r = RunnableLambda(lambda x: x + 1)
print(r.invoke(5))
```

---

## RunnableSequence

```python
r1 = RunnableLambda(lambda x: x + 1)
r2 = RunnableLambda(lambda x: x * 2)

chain = r1 | r2
print(chain.invoke(3))
```

---

## RunnableParallel

```python
from langchain_core.runnables import RunnableParallel

r = RunnableParallel({
    "add": RunnableLambda(lambda x: x + 1),
    "mul": RunnableLambda(lambda x: x * 2)
})

print(r.invoke(5))
```

---

## RunnableBranch

```python
from langchain_core.runnables import RunnableBranch

branch = RunnableBranch(
    (lambda x: x > 0, RunnableLambda(lambda x: "Positive")),
    (lambda x: x < 0, RunnableLambda(lambda x: "Negative")),
    RunnableLambda(lambda x: "Zero")
)

print(branch.invoke(10))
```

---

## RunnablePassthrough

```python
from langchain_core.runnables import RunnablePassthrough

r = RunnablePassthrough()
print(r.invoke({"name": "John"}))
```

---

## Real Pipeline Example

```python
pipeline = (
    RunnableLambda(lambda x: x * 2)
    | RunnableParallel({
        "square": RunnableLambda(lambda x: x**2),
        "cube": RunnableLambda(lambda x: x**3)
    })
)

print(pipeline.invoke(3))
```

---

## Methods

- invoke() → single input
- batch() → multiple inputs
- stream() → streaming output
- ainvoke() → async

---

## Key Insight

Runnables = Lego blocks for AI pipelines

---

## One-Liner

Runnables turn AI workflows into composable pipelines.
