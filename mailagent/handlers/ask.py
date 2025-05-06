# mailagent/handlers/ask.py

from mailagent.langchain.rag_engine import answer_with_context

def handle_ask(prompt: str, sender: str) -> str:
    """
    Handles the /ask command by returning an AI-generated response using approved facts.
    """
    if not prompt.strip():
        return "⚠️ No question provided in /ask command."

    return answer_with_context(prompt)
