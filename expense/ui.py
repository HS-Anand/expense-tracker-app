import tkinter as tk
from logic import TransactionManager
from insights import get_insights

def launch_ui():
    manager = TransactionManager()

    def add_transaction():
        payer = entry_payer.get().strip()
        try:
            amount = float(entry_amount.get())
        except:
            lbl_output.config(text="Invalid amount.")
            return
        people = [p.strip() for p in entry_people.get().split(",") if p.strip()]
        if not payer or not people:
            lbl_output.config(text="Fill all fields properly.")
            return

        manager.add_transaction(payer, amount, people)
        lbl_output.config(text="Transaction added.")
        entry_payer.delete(0, tk.END)
        entry_amount.delete(0, tk.END)
        entry_people.delete(0, tk.END)

    def show_result():
        result = manager.calculate_settlements()
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, "\n".join(result if result else ["All settled."]))

    def show_insights():
        insights = get_insights(manager.transactions)
        text_output.delete(1.0, tk.END)
        text_output.insert(tk.END, insights)

    root = tk.Tk()
    root.title("Smart Expense Splitter")
    root.geometry("680x530")
    root.config(bg="#e0f7f1")

    tk.Label(root, text="Smart Expense Splitter", font=("Segoe UI", 18, "bold"), bg="#e0f7f1", fg="#00796B").pack(pady=10)

    frm = tk.Frame(root, bg="#e0f7f1")
    frm.pack(pady=5)

    tk.Label(frm, text="Paid by:", bg="#e0f7f1").grid(row=0, column=0, padx=5)
    entry_payer = tk.Entry(frm, width=30)
    entry_payer.grid(row=0, column=1, padx=5)

    tk.Label(frm, text="Amount (₹):", bg="#e0f7f1").grid(row=1, column=0, padx=5)
    entry_amount = tk.Entry(frm, width=30)
    entry_amount.grid(row=1, column=1, padx=5)

    tk.Label(frm, text="Split Between (comma separated):", bg="#e0f7f1").grid(row=2, column=0, padx=5)
    entry_people = tk.Entry(frm, width=30)
    entry_people.grid(row=2, column=1, padx=5)

    lbl_output = tk.Label(root, text="", bg="#e0f7f1", fg="red")
    lbl_output.pack()

    btns = tk.Frame(root, bg="#e0f7f1")
    btns.pack(pady=5)
    tk.Button(btns, text="Add Transaction", bg="#00796B", fg="black", font=("Segoe UI", 10), command=add_transaction).grid(row=0, column=0, padx=10)
    tk.Button(btns, text="Show Settlements", bg="#004D40", fg="black", font=("Segoe UI", 10), command=show_result).grid(row=0, column=1, padx=10)
    tk.Button(btns, text="Show Insights", bg="#004D40", fg="black", font=("Segoe UI", 10), command=show_insights).grid(row=0, column=2, padx=10)

    text_output = tk.Text(root, width=75, height=16, bg="white", fg="black")
    text_output.pack(pady=10)

    root.mainloop()
