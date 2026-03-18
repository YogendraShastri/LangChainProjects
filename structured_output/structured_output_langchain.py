from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


load_dotenv()

class Review(BaseModel):
    summary: str = Field(description="1-2 line summary of the review")
    sentiment: str = Field(description="overall sentiment, e.g. positive/negative/neutral")

model = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

structured_output_model = model.with_structured_output(Review)


result = structured_output_model.invoke(
    "this was a worst mobile, very slow and lags sometimes, please return my money back"
)

print(result)

"""
summary='The mobile phone is very slow and lags frequently, leading to dissatisfaction.' 
sentiment='negative'
"""