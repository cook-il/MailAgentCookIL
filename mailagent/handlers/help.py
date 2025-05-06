# mailagent/handlers/help.py

def handle_help() -> str:
    return (
        "📬 MailAgentCookIL Command Guide:\n\n"
        "/ask [question]\n"
        "  → Get an AI-generated answer using approved local facts.\n\n"
        "/fact [statement]\n"
        "  → Submit a factual statement for admin review and training.\n\n"
        "/rag [referenceable text]\n"
        "  → Submit a paragraph or linkable source for retrieval-based QA.\n\n"
        "/help\n"
        "  → Show this help message.\n\n"
        "⚠️ One command per email. HTML or attachments are rejected."
    )
