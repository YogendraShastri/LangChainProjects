from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv()

json_schema = {
    "title": "Review",
    "description": "Extract a short summary and sentiment from a customer review.",
    "type": "object",
    "properties": {
        "summary": {
            "type": "string",
            "description": "1-2 line summary of the review",
        },
        "sentiment": {
            "type": "string",
            "description": "overall sentiment, e.g. positive/negative/neutral",
        },
    },
    "required": ["summary", "sentiment"],
    "additionalProperties": False,
}

model = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

structured_output_model = model.with_structured_output(json_schema)


result = structured_output_model.invoke(
    "this was a worst mobile, very slow and lags sometimes, please return my money back"
)

print(result)

"""
summary='The mobile phone is very slow and lags frequently, leading to dissatisfaction.' 
sentiment='negative'
"""