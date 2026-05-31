from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_docs():
    loader = DirectoryLoader(
        "data",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"},
    )

    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 2000,
        chunk_overlap = 200
    )

    return splitter.split_documents(docs)

