# mailagent/langchain/rag_engine.py

import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from mailagent.database.db import get_connection

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in .env")

llm = ChatOpenAI(model="gpt-4", temperature=0.2)

def fetch_context_snippets(limit=10) -> str:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT type, content, source FROM knowledge_base
        WHERE approved_by_admin = 1
        ORDER BY created_at DESC LIMIT ?
    """, (limit,))
    entries = cursor.fetchall()
    conn.close()

    if not entries:
        return "(No context found. Answer using general knowledge.)"

    formatted = []
    for t, content, source in entries:
        line = f"- ({t.upper()}) {content}"
        if source:
            line += f" [source: {source}]"
        formatted.append(line)

    return "\n".join(formatted)

# Template includes injected context block
prompt = PromptTemplate.from_template(
    "Use the following approved facts and references to help answer the question.\n\n"
    "CONTEXT:\n{context}\n\n"
    "QUESTION:\n{question}\n\n"
    "ANSWER:"
)

chain = prompt | llm

def answer_with_context(question: str) -> str:
    context = fetch_context_snippets()
    result = chain.invoke({"context": context, "question": question})
    return result.content.strip()
