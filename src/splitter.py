from langchain_text_splitters import RecursiveCharacterTextSplitter
from typing import List
from langchain_core.documents import Document

_SPLITTER = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # chunk size (characters)
    chunk_overlap=200,  # chunk overlap (characters)
    add_start_index=True,  # track index in original document
)

def split_docs(docs: List[Document]) -> List[Document]:
    """Divide documentos em chunks menores."""
    return _SPLITTER.split_documents(docs)

