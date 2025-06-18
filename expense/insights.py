import pandas as pd

def get_insights(transactions):
    if not transactions:
        return "No transactions available."

    df = pd.DataFrame(transactions)
    df_expanded = df.explode("split_between")

    payer_count = df["paid_by"].value_counts()
    payer_amount = df.groupby("paid_by")["amount"].sum()
    split_freq = df_expanded["split_between"].value_counts()

    result = []
    result.append("=== Spending Insights ===\n")

    result.append("Top Spenders:")
    for name, amount in payer_amount.items():
        result.append(f"- {name} paid a total of ₹{amount:.2f}")

    result.append("\nParticipation Frequency:")
    for name, count in split_freq.items():
        result.append(f"- {name} was part of {count} transaction(s)")

    result.append("\nMost Active Payers:")
    for name, count in payer_count.items():
        result.append(f"- {name} paid {count} time(s)")

    return "\n".join(result)
