# MailAgentCookIL
Successor to LangAgentMail, a secure AI-powered email agent using LangChain for structured reply and archival

## 🛠️ CLI Moderation Tool (`v1.1.0`)

MailAgentCookIL now includes a shell-based moderation interface for `/fact` and `/rag` entries.

### Usage

```bash
# List unapproved entries
python3 mailagent/tools/moderate.py list

# Approve multiple entries
python3 mailagent/tools/moderate.py approve 1 3 5

# Delete an entry
python3 mailagent/tools/moderate.py delete 4