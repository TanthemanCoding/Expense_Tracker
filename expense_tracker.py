import argparse
import json

def add_expenses(description, amount, expenses_file='expenses.json'):
    try:
        with open(expenses_file, "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []
        
    expenses.append({"description": description, "amount": amount})

    with open(expenses_file, "w") as f:
        json.dump(expenses, f, indent=4)


parser = argparse.ArgumentParser()
parser.add_argument("--description")
parser.add_argument("--amount", type=float)
expenses_1 = parser.parse_args()

add_expenses(expenses_1.description, expenses_1.amount)
    if expenses_1.description is None or expenses_1.amount is None:
        print("Please provide both description and amount.")






