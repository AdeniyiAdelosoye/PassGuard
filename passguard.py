import tkinter as tk
from password_analyzer import analyze_password
from password_generator import generate_password

def check_password():
    password = password_entry.get()

    strength, suggestions= analyze_password(password)

    result = f"Strength: {strength}\n\n"

    if suggestions:
        result += f"Suggestions:\n"
        for item in suggestions:
            result += f"- {item}\n"

    result_label.config(text=result)

def create_password():
    password = generate_password()
    generate_label.config(text=f"Generated Password:\n{password}")



window = tk.Tk()
window.title("PassGuard")
window.geometry("600x500")

title_label = tk.Label(
    window,
    text="PassGuard",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=10)

password_label = tk.Label(
    window,
    text="Enter Password:"
)
password_label.pack()

password_entry = tk.Entry(
    window,
    width=30
)
password_entry.pack(pady=5)

analyze_button = tk.Button(
    window,
    text="Analyze Password",
    command=check_password
)
analyze_button.pack(pady=10)

result_label = tk.Label(
    window,
    text="",
    justify="left"
)
result_label.pack(pady=10)

generate_button = tk.Button(
    window,
    text="Generate Password",
    command=create_password
)
generate_button.pack(pady=20)

generate_label = tk.Label(
    window,
    text=""
)

generate_label.pack(pady=10)

window.mainloop()