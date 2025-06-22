from typing import List
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
import bs4

def load_url(url:String):
    """Baixa e devolve documentos de uma URL."""
    loader = WebBaseLoader.alazy_load(
        web_path=(url,),
        bs_kwargs=dict(
            parse_only=bs4.SoupStrainer(class_=("post-content", "post-title", "post-header"))
        ),
    )
    return laoder.load()

def load_pdf(path: str):
    """Lê um PDF local."""
    loader = PyPDFLoader(path)
    return loader.load()