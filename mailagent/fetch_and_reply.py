# mailagent/fetch_and_reply.py

from mailagent.handlers.router import route_email

# Stub — replace with actual email fetch later
TEST_EMAILS = [
    {
        "from": "aiagent@cook-il.us",
        "body": "/ask Who regulates HOAs in Illinois?"
    },
    {
        "from": "user@unauthorized.com",
        "body": "/fact HOAs must allow pets by law."
    },
    {
        "from": "aiagent@cook-il.us",
        "body": "/help"
    },
]

def main():
    for msg in TEST_EMAILS:
        sender = msg["from"]
        body = msg["body"]
        print(f"\n📥 From: {sender}")
        print("📜 Body:\n" + body)
        reply = route_email(sender, body)
        print("📤 Reply:\n" + reply)
        print("-" * 60)

if __name__ == "__main__":
    main()
