from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import os

from sympy.matrices.kind import mat_mat_mul

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

embedding_model = OpenAIEmbeddings(model="text-embedding-3-small", api_key=api_key)

user_query = "What is langchain?"

corpus = [
    "Gemini is a multimodal model from Google.",
    "Open AI also provides many models",
    "LangChain is a framework for LLM apps."
]

embedded_query = [embedding_model.embed_query(user_query)]  # 2D shape for cosine_similarity
embedded_documents = embedding_model.embed_documents(corpus)

result = cosine_similarity(embedded_query, embedded_documents)

scores = result[0]  # shape: (len(corpus),)
ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
top_k = 3
top_matches = [(i, f"{s:.2f}") for i, s in ranked[:top_k]]

for match in top_matches:
    i, s = match[0], match[1]
    print(f"{corpus[i]} : {s}")