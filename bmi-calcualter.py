import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            raise ValueError

        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)

        if bmi < 18.5:
            result = "Underweight"
            color = "blue"
        elif bmi < 25:
            result = "Normal"
            color = "green"
        elif bmi < 30:
            result = "Overweight"
            color = "orange"
        else:
            result = "Obese"
            color = "red"

        result_label.config(text=f"BMI: {bmi}\nResult: {result}", fg=color)

        show_graph(bmi)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def show_graph(bmi):
    categories = ["Underweight", "Normal", "Overweight", "Obese"]
    ranges = [18.5, 25, 30, 40]

    plt.figure(figsize=(6,4))
    plt.bar(categories, ranges, color=["blue", "green", "orange", "red"])
    plt.axhline(y=bmi, color="black", linestyle="--", label=f"Your BMI: {bmi}")

    plt.ylabel("BMI Value")
    plt.title("BMI Category Chart")
    plt.legend()
    plt.tight_layout()
    plt.show()

# ---------------- UI ----------------

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x300")
root.resizable(False, False)

tk.Label(root, text="BMI Calculator", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Height (m):").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg="#4CAF50", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()