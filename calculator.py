
import tkinter as tk
from tkinter import messagebox
import math

# Global theme flag
is_dark_mode = False

# Evaluate the expression
def click(event):
    current = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text in ["sin", "cos", "tan", "sqrt", "pi"]:
        try:
            if button_text == "pi":
                entry.insert(tk.END, str(math.pi))
            else:
                expression = entry.get()
                value = float(eval(expression))
                result = getattr(math, button_text)(value)
                entry.delete(0, tk.END)
                entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, button_text)

# Keyboard input handler
def key_press(event):
    key = event.char
    if key in "0123456789+-*/().":
        entry.insert(tk.END, key)
    elif key == "\r":
        click(type('event', (object,), {'widget': type('btn', (object,), {'cget': lambda s: "="})})())

# Toggle dark mode
def toggle_theme():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    update_theme()

def update_theme():
    bg = "#222" if is_dark_mode else "#f4f4f4"
    fg = "#eee" if is_dark_mode else "#333"
    entry.config(bg=bg, fg=fg, insertbackground=fg)
    frame.config(bg=bg)
    theme_btn.config(text="Dark Mode" if not is_dark_mode else "Light Mode")

    for btn in buttons:
        btn.config(bg=bg, fg=fg, activebackground="#444" if is_dark_mode else "#e6e6e6")

# Main window
root = tk.Tk()
root.title("Pro Calculator")
root.geometry("360x520")
root.configure(bg="#f4f4f4")
root.bind("<Key>", key_press)

# Entry widget
entry = tk.Entry(root, font="Arial 20", bd=8, relief=tk.FLAT, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Theme toggle button
theme_btn = tk.Button(root, text="Dark Mode", command=toggle_theme, font=("Arial", 10), bg="#ffffff", relief=tk.GROOVE)
theme_btn.pack(pady=5)

# Button layout
button_layout = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["(", ")", ".", "pi"],
    ["sin", "cos", "tan", "sqrt"]
]

# Button style
buttons = []
frame = tk.Frame(root, bg="#f4f4f4")
frame.pack()

for row in button_layout:
    button_row = tk.Frame(frame, bg="#f4f4f4")
    button_row.pack(expand=True, fill="both")
    for item in row:
        btn = tk.Button(button_row, text=item, font=("Arial", 16), bg="#ffffff", fg="#333333", relief=tk.GROOVE, borderwidth=1)
        btn.pack(side="left", expand=True, fill="both", padx=4, pady=4)
        btn.bind("<Button-1>", click)
        buttons.append(btn)

update_theme()
root.mainloop()
