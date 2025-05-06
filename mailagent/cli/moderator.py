# mailagent/cli/moderator.py

import argparse
from mailagent.database.db import fetch_unapproved_entries, approve_entry, delete_entry

def list_unapproved():
    entries = fetch_unapproved_entries()
    if not entries:
        print("✅ No unapproved entries.")
        return

    print("🕵️ Unapproved Knowledge Base Entries:")
    for e in entries:
        print(f"[{e[0]}] {e[2].upper()} by {e[1]} — {e[3]}")
        if e[4]: print(f"    Source: {e[4]}")
        print("")

def approve(id_):
    approve_entry(id_)
    print(f"✅ Entry {id_} approved.")

def delete(id_):
    delete_entry(id_)
    print(f"🗑️ Entry {id_} deleted.")

def main():
    parser = argparse.ArgumentParser(description="Moderate unapproved knowledge base entries")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--list", action="store_true", help="List all unapproved entries")
    group.add_argument("--approve", type=int, metavar="ID", help="Approve entry by ID")
    group.add_argument("--delete", type=int, metavar="ID", help="Delete entry by ID")

    args = parser.parse_args()

    if args.list:
        list_unapproved()
    elif args.approve:
        approve(args.approve)
    elif args.delete:
        delete(args.delete)

if __name__ == "__main__":
    main()
