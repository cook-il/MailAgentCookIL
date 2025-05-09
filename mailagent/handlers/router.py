# mailagent/handlers/router.py

from mailagent.database.db import insert_message
from mailagent.handlers.ask import handle_ask
from mailagent.handlers.fact import handle_fact
from mailagent.handlers.rag import handle_rag
from mailagent.handlers.help import handle_help
from mailagent.handlers.link import handle_link


VALID_COMMANDS = {
    "/ask": handle_ask,
    "/fact": handle_fact,
    "/rag": handle_rag,
    "/help": lambda *_: handle_help(),
    "/link": handle_link,
}

def route_email(sender: str, body: str) -> str:
    """
    Parses a plain-text email body and routes it to the correct handler.
    Stores the message in the database if valid.
    Returns a reply string, or '__DISCARD__' to indicate no action needed.
    """
    lines = body.strip().splitlines()
    if not lines:
        return "__DISCARD__"

    first_line = lines[0].strip()
    if not first_line.startswith("/"):
        print("⚠️ Ignoring email: No command prefix.")
        return "__DISCARD__"

    parts = first_line.split(maxsplit=1)
    command = parts[0].lower()
    rest_of_body = parts[1] if len(parts) > 1 else ""

    if command not in VALID_COMMANDS:
        print(f"⚠️ Ignoring email: Unknown command {command}")
        return "__DISCARD__"

    # Log the message
    insert_message(sender, command, body.strip())

    # Route to appropriate handler
    handler = VALID_COMMANDS[command]
    if command in ["/ask", "/fact", "/rag", "/link"]:
        return handler(sender, rest_of_body)
    else:
        return handler()
