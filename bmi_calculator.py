import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

# DATABASE SETUP
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS bmi_records (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    weight REAL,
    height REAL,
    bmi REAL,
    category TEXT,
    date TEXT
)
""")
conn.commit()

# BMI CALCULATION
def calculate_bmi():
    name = entry_name.get().strip()
    weight = entry_weight.get().strip()
    height = entry_height.get().strip()

    
    if not name:
        messagebox.showerror("Error", "Name is required!")
        return

    try:
        weight = float(weight)
        height = float(height)

        if weight <= 0 or height <= 0:
            raise ValueError

    except:
        messagebox.showerror("Error", "Enter valid positive numbers!")
        return

    # BMI
    bmi = weight / (height ** 2)

    # Category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    result_label.config(text=f"BMI: {bmi:.2f} ({category})")

    # Save to DB
    cursor.execute("""
    INSERT INTO bmi_records (name, weight, height, bmi, category, date)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (name, weight, height, bmi, category, datetime.now().strftime("%Y-%m-%d %H:%M")))
    conn.commit()


#HISTORY 
def view_history():
    name = entry_name.get().strip()

    if not name:
        messagebox.showerror("Error", "Enter name first!")
        return

    cursor.execute("SELECT date, bmi FROM bmi_records WHERE name=?", (name,))
    records = cursor.fetchall()

    history_text.delete("1.0", tk.END)

    if not records:
        history_text.insert(tk.END, "No records found.\n")
        return

    for record in records:
        history_text.insert(tk.END, f"{record[0]} → BMI: {record[1]:.2f}\n")


#GRAPH
def show_graph():
    name = entry_name.get().strip()

    if not name:
        messagebox.showerror("Error", "Enter name first!")
        return

    cursor.execute("SELECT date, bmi FROM bmi_records WHERE name=?", (name,))
    records = cursor.fetchall()

    if not records:
        messagebox.showinfo("Info", "No data available to plot!")
        return

    dates = [r[0] for r in records]
    bmis = [r[1] for r in records]

    plt.figure()
    plt.plot(dates, bmis, marker='o')
    plt.title(f"BMI Trend for {name}")
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# GUI 
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("400x500")

# Title
tk.Label(root, text="BMI Calculator", font=("Arial", 18)).pack(pady=10)

# Name
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

# Weight
tk.Label(root, text="Weight (kg)").pack()
entry_weight = tk.Entry(root)
entry_weight.pack()

# Height
tk.Label(root, text="Height (m)").pack()
entry_height = tk.Entry(root)
entry_height.pack()

# Buttons
tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)
tk.Button(root, text="View History", command=view_history).pack(pady=5)
tk.Button(root, text="Show Graph", command=show_graph).pack(pady=5)

# Result
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# History box
history_text = tk.Text(root, height=10)
history_text.pack(pady=10)

# Run app
root.mainloop()
