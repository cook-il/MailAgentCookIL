import re
from mailagent.database.db import insert_message, fetch_all_messages

def handle_link(sender, body):
    body = body.replace("“", '"').replace("”", '"').replace("‘", "'").replace("’", "'")
    match = re.search(r'["\'](https?://[^"\']+)["\']', body.strip())
    if not match:
        return f"❌ Link rejected: please wrap your link in quotes. Input was:\n{body.strip()}"

    url = match.group(1)

    # Check for duplicates
    existing_links = [
        msg["body"] for msg in fetch_all_messages()
        if msg["command"] == "/link"
    ]
    if url in existing_links:
        return "⚠️ Link rejected: already submitted."

    # Store the link
    insert_message(sender, "/link", url)

    return f"✅ Link accepted and recorded:\n{url}"
