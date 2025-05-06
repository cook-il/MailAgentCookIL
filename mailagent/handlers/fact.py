# mailagent/handlers/fact.py

from mailagent.database.db import insert_knowledge_entry

TRUSTED_DOMAINS = ("cook-il.us", "kane-il.us", "dupage-il.us")  # Extend as needed

def is_trusted_sender(sender: str) -> bool:
    return any(sender.endswith("@" + domain) for domain in TRUSTED_DOMAINS)


def handle_fact(fact_content: str, sender: str, source: str = None) -> str:
    """
    Handles the /fact command to store a new unapproved knowledge entry.
    """
    if not is_trusted_sender(sender):
        return "⛔ Unauthorized: You are not allowed to submit facts."

    if not fact_content.strip():
        return "⚠️ No fact content provided."

    insert_knowledge_entry(sender, "fact", fact_content.strip(), source)
    return "✅ Fact submitted for review."
