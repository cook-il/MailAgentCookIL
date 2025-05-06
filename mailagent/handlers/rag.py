# mailagent/handlers/rag.py

from mailagent.database.db import insert_knowledge_entry

TRUSTED_DOMAINS = ("cook-il.us", "kane-il.us", "dupage-il.us")  # Shared with fact

def is_trusted_sender(sender: str) -> bool:
    return any(sender.endswith("@" + domain) for domain in TRUSTED_DOMAINS)


def handle_rag(content: str, sender: str, source: str = None) -> str:
    """
    Handles the /rag command to store retrievable RAG data.
    """
    if not is_trusted_sender(sender):
        return "⛔ Unauthorized: You are not allowed to submit RAG data."

    if not content.strip():
        return "⚠️ No content provided in /rag command."

    insert_knowledge_entry(sender, "rag", content.strip(), source)
    return "✅ RAG entry submitted for review."
