import os

from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate, load_prompt
from langchain_openai import OpenAI

def _read_int(prompt_text: str, *, min_value: int = 1) -> int:
    while True:
        raw = input(prompt_text).strip()
        try:
            value = int(raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if value < min_value:
            print(f"Please enter a value >= {min_value}.")
            continue
        return value


def main() -> None:
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")

    topic = input("Enter a topic: ").strip()
    if not topic:
        raise ValueError("Topic cannot be empty.")

    lines = _read_int("How many lines should the intro be? ", min_value=1)

    # prompt = PromptTemplate(
    #     template=(
    #         "You are a helpful assistant.\n"
    #         "Write an introduction about the topic: {topic}\n"
    #         "Constraints:\n"
    #         "- Exactly {lines} lines\n"
    #         "- Clear and beginner-friendly\n"
    #     ),
    #     input_variables=["topic", "lines"],
    # )
    prompt = load_prompt(f"{os.getcwd()}/prompts/template.json")

    llm = OpenAI(api_key=api_key, temperature=1.2)
    chain = prompt | llm

    result = chain.invoke({"topic": topic, "lines": lines})
    print("\n--- Output ---\n")
    print(result)


if __name__ == "__main__":
    main()

