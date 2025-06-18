# 💸 Smart Expense Tracker App

A Python-based desktop app to split group expenses, track balances, and gain smart insights into user behavior. Built using Tkinter for GUI, JSON for persistent storage, and pandas for analytics — this project mimics tools like Splitwise, tailored for small teams, friends, and college groups.

---

## 🚀 Features

- ✅ Add shared expenses with payer and participants
- ✅ Automatically calculate and simplify who owes whom
- ✅ Show real-time debt settlements
- ✅ Persistent storage using JSON (no database setup needed)
- ✅ AI-powered behavior insights using `pandas`:
  - Top spenders
  - Most frequent participants
  - Group patterns
- ✅ Clean, pastel-themed GUI (built with Tkinter)
- ✅ Modular architecture (UI, logic, insights)

---


## 🧱 Tech Stack

- **Language**: Python 3  
- **GUI**: Tkinter  
- **Data Storage**: JSON  
- **Data Analysis**: pandas  
- *(No external database or backend needed)*

---

## 📁 Folder Structure

expense-tracker-app/
│
├── main.py # Entry point
├── ui.py # GUI layout and event logic
├── logic.py # Transaction management and settlement
├── insights.py # Behavioral analytics (AI-lite using pandas)
├── transactions.json # Auto-generated data file
└── README.md # You're reading it

---



## 📈 Sample Insights Output

=== Spending Insights ===

### Top Spenders:

Alice paid a total of ₹1200.00

Bob paid a total of ₹750.00

### Participation Frequency:

Alice was part of 6 transaction(s)

Bob was part of 5 transaction(s)

### Most Active Payers:

Alice paid 3 time(s)

Bob paid 2 time(s)

 --- 
## 🧠 Why This Project?

Most expense apps are either too bloated or online-only. This app is built to:
- Help students or small teams split expenses offline
- Practice GUI dev, data handling, and modular Python
- Add smart insights for AI/ML-ready thinking

---
