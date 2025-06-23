from langchain_community.vectorstores import Chroma
from typing import List
from langchain_core.documents import Document

class VectorStoreRepository:
    def __init__(self,persist_dir: str, embedding_fn):
         self.store = Chroma(
            persist_directory=persist_dir,
            embedding_function=embedding_fn,
            collection_name="knowledge_base",
        )
         
    def index_documents(self, chunks: List[Document]):
        self.store.add_documents(chunks)
        
    def similarity_search(self, query: str, k: int =4):
        return self.store.similarity_search(query, k=k)