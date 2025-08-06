from collections import defaultdict
from typing import List, Dict, Tuple
import pandas as pd

Expense = Tuple[str, float, List[str], str]  # (payer, amount, [beneficiaries], description)

def calculate_balances(expenses: List[Expense]) -> Dict[str, float]:
    paid = defaultdict(float)
    owed = defaultdict(float)

    for payer, amount, shared_by, description in expenses:
        paid[payer] += amount
        share = amount / len(shared_by)
        for person in shared_by:
            owed[person] += share

    net = {person: paid[person] - owed[person] for person in set(paid) | set(owed)}
    return net

def settle_debts(net: Dict[str, float]) -> List[Tuple[str, str, float]]:
    debtors = [(p, -amt) for p, amt in net.items() if amt < 0]
    creditors = [(p, amt) for p, amt in net.items() if amt > 0]

    # Sort to ensure consistent greedy behavior
    debtors.sort(key=lambda x: x[1], reverse=True)
    creditors.sort(key=lambda x: x[1], reverse=True)

    settlements = []

    i, j = 0, 0
    while i < len(debtors) and j < len(creditors):
        debtor, debt_amt = debtors[i]
        creditor, cred_amt = creditors[j]

        amount = min(debt_amt, cred_amt)
        settlements.append((debtor, creditor, round(amount, 2)))

        debt_amt -= amount
        cred_amt -= amount

        if debt_amt == 0:
            i += 1
        else:
            debtors[i] = (debtor, debt_amt)

        if cred_amt == 0:
            j += 1
        else:
            creditors[j] = (creditor, cred_amt)

    return settlements

def dump_expenses_to_csv(expenses: List[Expense], csv_path: str = "expenses.csv") -> None:
    """
    Convert a list of Expense tuples to a CSV file.

    Parameters
    ----------
    expenses : list[Expense]
        Each Expense is (payer, amount, beneficiaries, description).
    csv_path : str, optional
        Output filename. Defaults to 'expenses.csv'.

    Notes
    -----
    * Beneficiaries are stored in a single cell, separated by '; ' so the list
      survives round-tripping.
    * The CSV is written without the pandas index and in UTF-8 encoding.
    """
    # Build a DataFrame
    df = pd.DataFrame(
        expenses,
        columns=["payer", "amount", "beneficiaries", "description"]
    )

    # Serialize the beneficiaries list into a readable string
    df["beneficiaries"] = df["beneficiaries"].apply("; ".join)

    # Persist to CSV
    df.to_csv(csv_path, index=False, encoding="utf-8")

def dump_expenses_to_markdown(expenses: List[Expense]) -> str:
    """Return a Markdown table representation of the expenses list."""
    df = pd.DataFrame(expenses,
                      columns=["payer", "amount", "beneficiaries", "description"])
    # serialise list → readable string
    df["beneficiaries"] = df["beneficiaries"].apply("; ".join)
    return df.to_markdown(index=False)

if __name__ == '__main__':
    expenses = [
        ("Antonio", 20.0, ["Antonio", "Luca"], "Parcheggio (20 €)"),
        ("Antonio", 10.0, ["Antonio", "Luca", "Valentino"], "Autostrada (10 €)"),
        ("Antonio", 23.0, ["Antonio", "Luca", "Valentino"], "Benzina (23 €)"),
        ("Antonio", 40.0, ["Antonio", "Luca", "Valentino"], "Pedaggio andata (40 €)"),
        ("Antonio", 5.0, ["Antonio", "Luca", "Valentino"], "Parcheggio (5 €)"),
        ("Luca", 24.0, ["Antonio", "Luca"], "Pranzo in spiaggia (24 €)"),
        ("Luca", 4.0, ["Antonio", "Luca"], "Caffè leccese (4 €)"),
        ("Antonio", 163.0, ["Antonio", "Luca", "Valentino"], "Cena (163 €)"),
        ("Antonio", 18.0, ["Antonio", "Luca", "Valentino"], "Birra (18 €)"),
        ("Valentino", 15.6, ["Antonio", "Luca", "Valentino"], "Colazione (15,60 €)"),
        ("Antonio", 8.4, ["Antonio", "Luca", "Valentino"], "Spesa varia (8,40 €)"),
        ("Valentino", 75.0, ["Antonio", "Luca", "Valentino"], "Noleggio barca (75 €)"),
        ("Luca", 24.0, ["Antonio", "Luca", "Valentino"], "Stracetti (24 €)"),
        ("Luca", 8.0, ["Luca", "Valentino"], "Birra (8 €)"),
        ("Valentino", 16.0, ["Antonio", "Luca", "Valentino"], "Bombette (16 €)"),
        ("Luca", 16.0, ["Antonio", "Luca", "Valentino"], "Bruschette con capocollo (16 €)"),
        ("Antonio", 13.5, ["Antonio", "Valentino"], "Birra e patatine Porto Cesario"),
        ("Antonio", 18.5, ["Antonio", "Luca", "Valentino"], "Aperitivo Skafè al Casotto (frutta pessima)"),
        ("Antonio", 65, ["Antonio", "Luca", "Valentino"], "Benzina andata/ritorno"),
        ("Antonio", 47, ["Antonio", "Valentino"], "Pranzo Punta Prosciutto"),
        ("Antonio", 38.8, ["Antonio", "Luca", "Valentino"], "Pedaggio ritorno (38,80 €)"),
    ]

    net = calculate_balances(expenses)
    print("Net balances:")
    for person, balance in net.items():
        print(f"{person}: {round(balance, 2)}")

    print("\nSettlements:")
    for debtor, creditor, amount in settle_debts(net):
        print(f"{debtor} pays {amount} to {creditor}")

    dump_expenses_to_csv(expenses, 'puglia_trip.csv')
    print("\nSummary:")
    print(dump_expenses_to_markdown(expenses))