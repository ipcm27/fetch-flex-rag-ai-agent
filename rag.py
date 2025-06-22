import getpass
import os
import faiss

from langchain_openai import OpenAIEmbeddings
from langchain.chat_models import init_chat_model

if not os.environ.get("OPENAI_API_KEY"):
  os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")


llm = init_chat_model("gpt-4o-mini", model_provider="openai")
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

print(faiss.__version__)