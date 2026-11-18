import sys
import json
import os
from datetime import date

FILE = "expenses.json"

def load_expenses():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def save_expenses(expenses):
    with open(FILE, "w") as f:
        json.dump(expenses, f, indent=2)

def main():
    if len(sys.argv) < 2:
        print("Usage: python tracker.py [add|list|total] ...")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 4:
            print('Usage: python tracker.py add <amount> <category>')
            sys.exit(1)

        try:
            amount = float(sys.argv[2])
        except ValueError:
            print("Amount must be a number")
            sys.exit(1)

        category = sys.argv[3]
        note = " ".join(sys.argv[4:]) if len(sys.argv) > 4 else ""

        expenses = load_expenses()
        expenses.append({
            "amount": amount,
            "category": category.lower(),
            "date": str(date.today()),
            "note": note
        })
        save_expenses(expenses)
        print(f"Added: {amount} for {category}")

    elif command == "list":
        expenses = load_expenses()
        if not expenses:
            print("No expenses yet")
        else:
            for i, e in enumerate(expenses, 1):
                note_part = f" - {e['note']}" if e['note'] else ""
                print(f"{i}. [{e['date']}] {e['category']} - {e['amount']}{note_part}")

    elif command == "total":
        expenses =load_expenses()
        if len(sys.argv) > 2:
            category = sys.argv[2].lower()
            total = sum(e["amount"] for e in expenses if e["category"] == category)
            print(f"Total for {category}: {total}")
        else:
            total = sum(e["amount"] for e in expenses)
            print(f"Total expenses: {total}")

    else:
        print("Unknown command")

if __name__ == "__main__":
    main()