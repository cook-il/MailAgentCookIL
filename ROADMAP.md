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
- [ ] `cli/`: simple moderation tool to approve facts/rags

---

## 🔁 v1.1.0 — Admin Moderation Tool (CLI Focus)

**Status:** Planned  
**Goal:** Enable manual approval and deletion of submitted `/fact` and `/rag` entries

### Features
- [ ] CLI interface for:
  - Listing unapproved entries
  - Approving individual or batch entries
  - Deleting malformed or malicious entries
- [ ] Logging and confirmation prompts for all moderation actions

---

## 🧪 v1.2.0 — Testing, Resilience & Logging

**Status:** Planned  
**Goal:** Harden the system for edge cases and improve observability

### Features
- [ ] Robust error handling (invalid command formats, DB write failures)
- [ ] Daily log rotation or pruning
- [ ] Email ID / hash deduplication logic
- [ ] CLI command to inspect stored message history

---

## 🚀 v2.0.0 — Expansion & Optional Web GUI (TBD)

**Status:** Future  
**Goal:** Explore optional GUI for admin moderation while maintaining full offline CLI parity

### Optional Features
- [ ] Lightweight web dashboard for reviewing `/fact` and `/rag` submissions
- [ ] Role-based access control for multiple admins
- [ ] Metrics dashboard (counts, per-user stats, etc.)

---

## 🔒 Long-Term Security Goals

- [ ] DKIM/SPF enforcement and logging
- [ ] PGP integration for signed email verification
- [ ] Optional message integrity hashing per entry
- [ ] Rate limiting and IP logging (optional)

---

## 🗂 Supporting Files and Standards

- `TAGS.md`: Maintain topic classification for RAG facts
- `IDENTITIES.md`: Authoritative list of trusted agents
- `CONTRIBUTING.md`: Contributor guidelines and command rules

---

## 📍 Current Location

All development is taking place in:
