# rag_service.py
from typing import List
from langchain_core.documents import Document
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

_RAG_PROMPT = ChatPromptTemplate.from_template("""
Answer the question using **only** the context below.
If you don't know, say "I don't know.".

Context:
{context}

Question:
{question}

Resposta:
""")

class RAGService:
    def __init__(self, vector_repo, model_name="gpt-4o-mini"):
        self.store = vector_repo
        self.llm = init_chat_model(model_name, model_provider="openai")
    
    def _format_context(self, docs: List[Document]) -> str:
        return "\n\n".join(d.page_content for d in docs)

    def answer(self, question: str, k: int = 4) -> str:
        docs = self.store.similarity_search(question, k=k)
        context = self._format_context(docs)
        prompt = _RAG_PROMPT.invoke({"question": question, "context": context})
        response = self.llm.invoke(prompt)
        return response.content
    
    