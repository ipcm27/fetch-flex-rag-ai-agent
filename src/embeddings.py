from langchain_openai import OpenAIEmbeddings 
import os, getpass

def get_embedding_model():
    """ Return the instance of embeeding from OpenAI """
    if not os.getenv("OPENAI_API_KEY"):
         os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")
    return OpenAIEmbeddings(model="text-embedding-3-large")