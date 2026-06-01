from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from app.embeddings import get_embeddings
from app.prompts import ARCHIVIST_PROMPT, SUMMARY_PROMPT

load_dotenv()

conversation_summary = ""

embedding_model = get_embeddings()

vectorstore = FAISS.load_local(
    "faiss_index",
    embedding_model,
    allow_dangerous_deserialization=True
)

retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.9
)

parser = StrOutputParser()


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def get_history(_):
    return conversation_summary


answer_chain = (
    {
        "context": retriever | format_docs,
        "history": get_history,
        "question": RunnablePassthrough()
    }
    | ARCHIVIST_PROMPT
    | model
    | parser
)


summary_chain = (
    SUMMARY_PROMPT
    | model
    | parser
)


def update_summary(question, answer):
    global conversation_summary

    conversation_summary = summary_chain.invoke({
        "old_summary": conversation_summary,
        "question": question,
        "answer": answer
    })


def ask(question):
    answer = answer_chain.invoke(question)
    update_summary(question, answer)
    return answer


if __name__ == "__main__":
    while True:
        question = input("\nAsk the archive: ")

        if question.lower() in ["exit", "quit"]:
            break

        answer = ask(question)
        print("\nArchivist:", answer)