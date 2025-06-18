from collections import defaultdict
import json
import os

DATA_FILE = "transactions.json"

class TransactionManager:
    def __init__(self):
        self.transactions = []
        self.load_transactions()

    def save_transactions(self):
        with open(DATA_FILE, "w") as f:
            json.dump(self.transactions, f)

    def load_transactions(self):
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as f:
                self.transactions = json.load(f)

    def add_transaction(self, paid_by, amount, people):
        self.transactions.append({
            "paid_by": paid_by,
            "amount": amount,
            "split_between": people
        })
        self.save_transactions()

    def calculate_settlements(self):
        balance = defaultdict(float)
        for txn in self.transactions:
            payer = txn["paid_by"]
            amount = txn["amount"]
            people = txn["split_between"]
            split_amt = amount / len(people)
            for person in people:
                balance[person] -= split_amt
            balance[payer] += amount

        debtors = []
        creditors = []
        for person, amt in balance.items():
            if amt < 0:
                debtors.append([person, -amt])
            elif amt > 0:
                creditors.append([person, amt])

        i = j = 0
        settlements = []
        while i < len(debtors) and j < len(creditors):
            d_name, d_amt = debtors[i]
            c_name, c_amt = creditors[j]
            paid = min(d_amt, c_amt)
            settlements.append(f"{d_name} pays ₹{paid:.2f} to {c_name}")
            debtors[i][1] -= paid
            creditors[j][1] -= paid
            if debtors[i][1] == 0:
                i += 1
            if creditors[j][1] == 0:
                j += 1

        return settlements
