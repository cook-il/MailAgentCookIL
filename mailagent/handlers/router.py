# mailagent/handlers/router.py

from mailagent.database.db import insert_message
from mailagent.handlers.ask import handle_ask
from mailagent.handlers.fact import handle_fact
from mailagent.handlers.rag import handle_rag
from mailagent.handlers.help import handle_help

VALID_COMMANDS = {
    "/ask": handle_ask,
    "/fact": handle_fact,
    "/rag": handle_rag,
    "/help": lambda *_: handle_help(),
}

def route_email(sender: str, body: str) -> str:
    """
    Parses a plain-text email body and routes it to the correct handler.
    Stores the message in the database.
    """
    lines = body.strip().splitlines()
    if not lines:
        return "⚠️ Empty message received."

    first_line = lines[0].strip()
    parts = first_line.split(maxsplit=1)
    command = parts[0].lower()
    rest_of_body = parts[1] if len(parts) > 1 else ""

    if command not in VALID_COMMANDS:
        return f"❌ Unknown command: {command}\nTry /help for supported options."

    # Log the message
    insert_message(sender, command, body.strip())

    # Route to appropriate handler
    handler = VALID_COMMANDS[command]
    if command in ["/ask", "/fact", "/rag"]:
        return handler(rest_of_body, sender)
    else:
        return handler()
