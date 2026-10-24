import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

llm = init_chat_model(
    model="azure_ai:gpt-5.6-luna",
    base_url=os.getenv("ENDPOINT"),
    api_key=api_key
)

response = llm.invoke("What is the capital of France?")
print(response.content)