import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
import os

# File for storing data
DATA_FILE = "financial_data.csv"

# Ensure the data file exists
if not os.path.exists(DATA_FILE):
    df = pd.DataFrame(columns=["Date", "Category", "Type", "Amount", "Description"])
    df.to_csv(DATA_FILE, index=False)

# Load data
def load_data():
    return pd.read_csv(DATA_FILE)

# Save data
def save_data(df):
    df.to_csv(DATA_FILE, index=False)

# Add a new entry
def add_entry():
    date = date_entry.get()
    category = category_entry.get()
    type_ = type_var.get()
    amount = amount_entry.get()
    description = description_entry.get()

    if not (date and category and type_ and amount):
        messagebox.showerror("Error", "All fields except Description are mandatory.")
        return

    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a valid number.")
        return

    df = load_data()
    new_entry = pd.DataFrame(
        {"Date": [date], "Category": [category], "Type": [type_], "Amount": [amount], "Description": [description]}
    )
    df = pd.concat([df, new_entry], ignore_index=True)
    save_data(df)
    refresh_table()
    clear_inputs()
    messagebox.showinfo("Success", "Entry added successfully!")

# Refresh the table
def refresh_table():
    for row in tree.get_children():
        tree.delete(row)
    df = load_data()
    for _, row in df.iterrows():
        tree.insert("", "end", values=list(row))

# Generate reports
def generate_report():
    df = load_data()
    if df.empty:
        messagebox.showinfo("Report", "No data available.")
        return

    total_income = df[df["Type"] == "Income"]["Amount"].sum()
    total_expense = df[df["Type"] == "Expense"]["Amount"].sum()
    balance = total_income - total_expense

    messagebox.showinfo(
        "Financial Report",
        f"Total Income: ₹{total_income:.2f}\nTotal Expense: ₹{total_expense:.2f}\nNet Balance: ₹{balance:.2f}",
    )

# Clear inputs
def clear_inputs():
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    description_entry.delete(0, tk.END)

# Delete all data
def clear_all_data():
    if messagebox.askyesno("Confirm", "Are you sure you want to delete all data?"):
        save_data(pd.DataFrame(columns=["Date", "Category", "Type", "Amount", "Description"]))
        refresh_table()
        messagebox.showinfo("Success", "All data cleared successfully.")

# GUI Setup
root = tk.Tk()
root.title("Expense and Income Tracker")

# Entry Frame
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

tk.Label(entry_frame, text="Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5)
date_entry = tk.Entry(entry_frame)
date_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(entry_frame, text="Category:").grid(row=1, column=0, padx=5, pady=5)
category_entry = tk.Entry(entry_frame)
category_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(entry_frame, text="Type:").grid(row=2, column=0, padx=5, pady=5)
type_var = tk.StringVar(value="Income")
income_rb = tk.Radiobutton(entry_frame, text="Income", variable=type_var, value="Income")
expense_rb = tk.Radiobutton(entry_frame, text="Expense", variable=type_var, value="Expense")
income_rb.grid(row=2, column=1, sticky="w", pady=5)
expense_rb.grid(row=2, column=1, sticky="e", pady=5)

tk.Label(entry_frame, text="Amount:").grid(row=3, column=0, padx=5, pady=5)
amount_entry = tk.Entry(entry_frame)
amount_entry.grid(row=3, column=1, padx=5, pady=5)

tk.Label(entry_frame, text="Description:").grid(row=4, column=0, padx=5, pady=5)
description_entry = tk.Entry(entry_frame)
description_entry.grid(row=4, column=1, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Entry", command=add_entry).grid(row=0, column=0, padx=5, pady=5)
tk.Button(button_frame, text="Generate Report", command=generate_report).grid(row=0, column=1, padx=5, pady=5)
tk.Button(button_frame, text="Clear All Data", command=clear_all_data).grid(row=0, column=2, padx=5, pady=5)

# Data Table
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10)

columns = ["Date", "Category", "Type", "Amount", "Description"]
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=10)
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100)

tree.pack(side=tk.LEFT)

scrollbar = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Populate Table
refresh_table()

root.mainloop()
