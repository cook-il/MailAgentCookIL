#!/usr/bin/env python3

import argparse
import sqlite3
import os
from tabulate import tabulate

DB_PATH = os.getenv("TEST_DB_PATH") or os.path.abspath(os.path.join(os.path.dirname(__file__), '../../mailagent.db'))

def connect():
    return sqlite3.connect(DB_PATH)

def list_pending():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT id, type, content, source, created_at FROM knowledge_base WHERE approved_by_admin = 0")
    rows = c.fetchall()
    conn.close()
    if not rows:
        print("No unapproved entries found.")
    else:
        print(tabulate(rows, headers=["ID", "Type", "Content", "Source", "Created At"]))

def approve_entry(entry_id):
    conn = connect()
    c = conn.cursor()
    c.execute("UPDATE knowledge_base SET approved_by_admin = 1 WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()
    print(f"[✓] Entry {entry_id} approved.")

def delete_entry(entry_id):
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM knowledge_base WHERE id = ?", (entry_id,))
    conn.commit()
    conn.close()
    print(f"[✗] Entry {entry_id} deleted.")

def main():
    parser = argparse.ArgumentParser(description="Moderate knowledge base entries.")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list", help="List unapproved entries")

    approve_parser = subparsers.add_parser("approve", help="Approve one or more entries")
    approve_parser.add_argument("ids", nargs="+", type=int, help="IDs of entries to approve")

    delete_parser = subparsers.add_parser("delete", help="Delete an entry")
    delete_parser.add_argument("id", type=int, help="ID of entry to delete")

    args = parser.parse_args()

    if args.command == "list":
        list_pending()
    elif args.command == "approve":
        for entry_id in args.ids:
            approve_entry(entry_id)
    elif args.command == "delete":
        delete_entry(args.id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
