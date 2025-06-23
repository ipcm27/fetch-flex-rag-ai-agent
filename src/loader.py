from typing import List
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
import bs4
import os
os.environ["USER_AGENT"] = "fetch-and-flex/0.1"

def load_url(url:str):
    """Baixa e devolve documentos de uma URL."""
    loader = WebBaseLoader(
        web_paths=(url,),
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(
                class_=("post-content", "post-title", "post-header")
            )
        ),
    )
    return loader.load()

def load_pdf(path: str):
    """Lê um PDF local."""
    loader = PyPDFLoader(path)
    return loader.load()