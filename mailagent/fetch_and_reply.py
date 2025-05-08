# mailagent/fetch_and_reply.py

from mailagent.email_client import fetch_unread_emails, delete_email, send_reply, log_interaction
from mailagent.handlers.router import route_email
from mailagent.database.db import insert_message

def main():
    messages = fetch_unread_emails()
    for sender, body, uid in messages:
        print(f"\n From: {sender}\n Body:\n{body}")
        try:
            reply = route_email(sender, body)
            if reply != "__DISCARD__":
                print(" Reply:\n", reply)
                send_reply(sender, reply)
                log_interaction(sender, body, reply)
            else:
                print("🛑 Discarded message without reply.")
        except Exception as e:
            error_reply = f"⚠️ Failed to process your command: {e}"
            print(" Error:\n", error_reply)
            send_reply(sender, error_reply)
            log_interaction(sender, body, error_reply)
        delete_email(uid)

if __name__ == "__main__":
    main()
