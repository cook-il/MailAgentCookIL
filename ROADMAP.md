# 🛤 ROADMAP: MailAgentCookIL

This roadmap outlines the development plan for `MailAgentCookIL`, the successor to LangAgentMail. The goal is to deliver a secure, plain-text, command-based email interface with a curated LangChain-backed AI engine.

---

## ✅ v1.0.0 — MVP Completion (Baseline Functionality)

**Status:** ✅ Completed  
**Goal:** End-to-end functioning pipeline from email intake to AI response using verified commands only.

### Core Features
- [x] Plain-text email filtering and rejection of HTML/multimedia
- [x] Single-command enforcement per email
- [x] SQLite logging of raw messages
- [x] Domain-verified sender enforcement
- [x] `OPENAI_API_KEY` stored via `.env`
- [x] Command parser: `/ask`, `/fact`, `/rag`, `/help`
- [x] LangChain integration using only approved knowledge base data

### Required Modules
- [x] `handlers/`: process each supported command
- [x] `database/`: schema for messages and knowledge_base
- [x] `langchain/`: isolated logic for generating responses
- [x] `tools/`: CLI-based moderation commands

---

## 🔁 v1.1.0 — Admin Moderation Tool (CLI Focus)

**Status:** Completed  
**Goal:** Enable manual approval and deletion of submitted `/fact` and `/rag` entries

### Features
- [x] CLI interface for:
  - [x] Listing unapproved entries
  - [x] Approving individual or batch entries
  - [x] Deleting malformed or malicious entries
- [x] Tested against an isolated database
- [x] `tabulate`-based output formatting
---

## 🧪 v1.2.0 — Web-Based Moderation (Web2Py Dashboard)

**Status:** In Progress  
**Goal:** Replace CLI moderation with a secure, browser-based admin panel

### Features
- [ ] Secure login (password-protected Web2Py admin)
- [ ] Moderation dashboard listing all unapproved entries
- [ ] Approve or delete entries from the web UI
- [ ] Action logging (moderator, timestamp, action type)
- [ ] Entry details and filters (by type, contributor, or keyword)
- [ ] Optional JSON API support for future UI reuse

---

## 🧭 Future Milestones

_(To be defined after v1.2.0 is complete)_