from langchain_community.vectorstores import FAISS

from app.loader import load_and_split_docs
from app.embeddings import get_embeddings


def ingest_docs():
    chunks = load_and_split_docs()
    embedding_model = get_embeddings()

    vectorstore = FAISS.from_documents(
        chunks,
        embedding_model
    )

    vectorstore.save_local("faiss_index")

    print("Saved FAISS index")
    print("Total chunks:", len(chunks))


if __name__ == "__main__":
    ingest_docs()