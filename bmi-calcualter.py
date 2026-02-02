import tkinter as tk

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            result = "Underweight"
            color = "#3498db"
        elif bmi < 25:
            result = "Normal"
            color = "#2ecc71"
        elif bmi < 30:
            result = "Overweight"
            color = "#f1c40f"
        else:
            result = "Obese"
            color = "#e74c3c"

        result_label.config(text=f"BMI: {bmi}\n{result}", fg=color)

        draw_circle(bmi, color)

    except ValueError:
        result_label.config(text="Please enter valid numbers", fg="red")

def draw_circle(bmi, color):
    canvas.delete("all")

    # Background circle
    canvas.create_oval(20, 20, 180, 180, outline="#444", width=12)

    # Limit BMI to 40 for display
    angle = min(bmi / 40 * 360, 360)

    # BMI Arc
    canvas.create_arc(
        20, 20, 180, 180,
        start=90,
        extent=-angle,
        style="arc",
        outline=color,
        width=12
    )

    # Center text
    canvas.create_text(
        100, 100,
        text=str(bmi),
        fill="white",
        font=("Arial", 16, "bold")
    )

# Window
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("350x480")
root.config(bg="#1e1e2f")

# Title
tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="#1e1e2f"
).pack(pady=15)

# Weight
tk.Label(root, text="Weight (kg)", fg="white", bg="#1e1e2f").pack()
weight_entry = tk.Entry(root, font=("Arial", 12))
weight_entry.pack(pady=5)

# Height
tk.Label(root, text="Height (m)", fg="white", bg="#1e1e2f").pack()
height_entry = tk.Entry(root, font=("Arial", 12))
height_entry.pack(pady=5)

# Button
tk.Button(
    root,
    text="Calculate BMI",
    command=calculate_bmi,
    bg="#9b59b6",
    fg="white",
    font=("Arial", 12),
    width=15
).pack(pady=15)

# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#1e1e2f"
)
result_label.pack(pady=10)

# Circular Graph Canvas
canvas = tk.Canvas(
    root,
    width=200,
    height=200,
    bg="#2c2c3c",
    highlightthickness=0
)
canvas.pack(pady=10)

root.mainloop()
