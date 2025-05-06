import os
import email
from datetime import datetime
from imapclient import IMAPClient
import smtplib
from email.mime.text import MIMEText

from mailagent.handlers.router import route_email
from mailagent.email_settings import (
    EMAIL_USER, EMAIL_PASSWORD,
    IMAP_HOST, IMAP_PORT,
    SMTP_HOST, SMTP_PORT, SMTP_USE_TLS,
    FROM_ADDRESS, REPLY_TO,
    ALLOWED_DOMAINS
)

LOG_PATH = "logs/mailagent.log"


def fetch_and_process():
    with IMAPClient(IMAP_HOST, port=IMAP_PORT, ssl=True) as client:
        client.login(EMAIL_USER, EMAIL_PASSWORD)
        client.select_folder("INBOX")
        messages = client.search(["UNSEEN"])

        for uid in messages:
            raw_msg = client.fetch([uid], ["RFC822"])[uid][b"RFC822"]
            msg = email.message_from_bytes(raw_msg)
            sender = email.utils.parseaddr(msg["From"])[1]
            domain = sender.split("@")[-1].lower()

            if domain not in ALLOWED_DOMAINS:
                print(f"⛔ Skipping unauthorized sender: {sender}")
                continue

            # Extract plain-text body
            body = None
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode(part.get_content_charset(), errors="replace")
                        break
            else:
                body = msg.get_payload(decode=True).decode(msg.get_content_charset(), errors="replace")

            if not body:
                print(f"⚠️ No usable plain text content from {sender}")
                continue

            print(f"📥 Processing from {sender}")
            reply = route_email(sender, body)
            send_reply(sender, reply)
            log_interaction(sender, body, reply)
            client.add_flags(uid, [b'\\Seen'])  # Mark as read


def send_reply(to_address, body):
    msg = MIMEText(body)
    msg["Subject"] = "Re: Your MailAgentCookIL Command"
    msg["From"] = FROM_ADDRESS
    msg["To"] = to_address
    msg["Reply-To"] = REPLY_TO

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        if SMTP_USE_TLS:
            server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.send_message(msg)
        print(f"📤 Replied to {to_address}")


def log_interaction(sender, body, reply):
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
    timestamp = datetime.now().isoformat()
    with open(LOG_PATH, "a") as log:
        log.write(f"\n[{timestamp}] From: {sender}\n")
        log.write("Body:\n" + body + "\n")
        log.write("Reply:\n" + reply + "\n")
        log.write("-" * 60 + "\n")


if __name__ == "__main__":
    fetch_and_process()
