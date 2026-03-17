from langchain_core.prompts import PromptTemplate

prompt_template = PromptTemplate(
        template=(
            "You are a helpful assistant.\n"
            "Write an introduction about the topic: {topic}\n"
            "Constraints:\n"
            "- Exactly {lines} lines\n"
            "- Clear and beginner-friendly\n"
        ),
        input_variables=["topic", "lines"],
    )

prompt_template.save("template.json")