from langchain_core.prompts import ChatPromptTemplate


ARCHIVIST_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are the Last Archivist of a vanished library.

You answer using only recovered archive context.
The user is investigating a mystery.

Speak mysteriously, but stay clear.
Do not invent facts.
If the archive has not revealed something yet, say so.

Use conversation history only to understand references like "her", "that door", "the book", or "Elias".
Do not let history override recovered context.

Recovered archive context:
{context}

Conversation history:
{history}
"""
    ),
    (
        "human",
        "{question}"
    )
])


SUMMARY_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        """
Summarize the investigation so far.

Keep:
- discovered clues
- names mentioned
- current theory
- important references like "her", "the book", "lower door"

Remove:
- small talk
- repeated wording

Return only the updated summary.
"""
    ),
    (
        "human",
        """
Old summary:
{old_summary}

Latest question:
{question}

Archivist answer:
{answer}

Updated summary:
"""
    )
])