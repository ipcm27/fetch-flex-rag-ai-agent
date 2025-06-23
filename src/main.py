import argparse, pathlib
from loader import load_url, load_pdf
from embeddings import get_embedding_model
from vector_store import VectorStoreRepository
from splitter import split_docs
from rag_service import RAGService
import os
os.environ["USER_AGENT"] = "fetch-and-flex/0.1"

def build_index(src: str):
    """carrega, diviide e indexa a font (PDF ou URL)"""
    if src.lower().startswith(("http://", "https://")):
        docs = load_url(src)
    else:
        path = pathlib.Path(src)
        if not path.exists():
            raise FileNotFoundError(path)
        docs = load_pdf(str(path))
    
    chunks = split_docs(docs)
    embeddings = get_embedding_model()
    repo = VectorStoreRepository("./db", embeddings)
    repo.index_documents(chunks)
    return repo

def main():

    parser = argparse.ArgumentParser(description="RAG CLI")
    parser.add_argument("source", help="PDF path or URl to index")
    args = parser.parse_args()
    
    repo = build_index(args.source)
    rag = RAGService(repo)
    
    print("\n ìndice criado! Faça perguntas ou digote 'sair' para sair.")
    while True:
        q = input("\nPergunta> ").strip()
        if q.lower() in {"sair", "exit"}:
            break
        print("\nResposta:", rag.answer(q))
        
if __name__ == "__main__":
    main()