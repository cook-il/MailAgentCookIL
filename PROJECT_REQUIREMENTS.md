# 📦 Project Requirements: MailAgentCookIL

This project is the successor to LangAgentMail, using the same infrastructure, mail routing, and trusted AI-agent identity.

---

## 🧭 Functional Goals for v1.0.0

- ✅ Command-based, plain-text email interface — **no web UI**
- ✅ AI responses are generated via LangChain using only approved, admin-reviewed facts and links
- ✅ All email inputs must be in plain text; **HTML/CSS/images are rejected**
- ✅ **One command per email** is enforced (e.g., `/ask`, `/fact`, `/rag`, `/help`)
- ✅ Only admin accounts (e.g., aiagent@kane-il.us) may contribute training data
- ✅ All commands are processed from verified sender domains only (e.g., `cook-il.us`, `kane-il.us`)
- ✅ Emails are deleted if:
  - No command is at the beginning of the body
  - HTML/CSS or multimedia is detected in the body
- ✅ Valid emails are logged in an SQLite datastore in raw, timestamped format
- ✅ LangChain uses only pre-approved RAG data from the SQLite-backed knowledge base
- ✅ `.env` file will be used to store environment variables including `OPENAI_API_KEY`

---

## 🧱 Code Architecture

```
mailagentcookil/
├── mailagent/
│   ├── __init__.py
│   ├── handlers/        # Command handlers (ask, help, fact, rag, etc.)
│   ├── database/        # SQLite interactions and schema
│   ├── langchain/       # LangChain response logic
│   └── cli/             # Admin tools for moderation, approval, etc.
├── .env
├── requirements.txt
├── ARCHIVE_README.md
├── ROADMAP.md
├── TAGS.md
├── IDENTITIES.md
└── CONTRIBUTING.md
```

---

## 🧑‍💼 Admin Review Process

- All `/fact` and `/rag` entries will be stored in the `knowledge_base` table with `approved_by_admin = 0` by default.
- Only approved entries will be visible to LangChain.
- A future CLI or web admin tool will be developed to allow moderators to review, approve, or delete queued entries.

---

## 🗄 Storage

**Messages Table** (`messages`):
- Raw email text (plain only)
- Timestamped
- One command per message

**Knowledge Base Table** (`knowledge_base`):
- Contributor email (verified only)
- Type: `fact` or `rag`
- Content: Normalized string input
- Source: Optional text
- approved_by_admin: Default `0`

---

## 📑 Supporting Files

- `TAGS.md`: Maintains taxonomy of tags used in `/tag` or metadata classification
- `IDENTITIES.md`: Trusted email identities and reserved namespaces
- `CONTRIBUTING.md`: Contributor rules, process flow, admin-level operations

---

## 🛡 Security and Filtering

- Incoming mail is filtered for:
  - Approved domain whitelist (via regex or explicit config)
  - Content type (plain only, reject HTML or MIME-rich)
- Valid messages are routed to SQLite for processing
- Invalid messages are silently dropped

---

## 🔄 Status

Ready to initialize new project in `/home/aiagent/mailagentcookil` using this document as the reference build plan.
