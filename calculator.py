
import tkinter as tk
from tkinter import messagebox
import math

# Global states
is_dark_mode = False
memory = 0
history = []

# Evaluate the expression
def click(event):
    global memory
    current = entry.get()
    button_text = event.widget.cget("text")

    if button_text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
            history.append(f"{current} = {result}")
            update_history()
        except:
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
                history.append(f"{button_text}({value}) = {result}")
                update_history()
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "M+":
        try:
            memory_value = float(eval(entry.get()))
            memory += memory_value
        except:
            pass
    elif button_text == "MR":
        entry.insert(tk.END, str(memory))
    elif button_text == "MC":
        memory = 0
    elif button_text == "Copy":
        root.clipboard_clear()
        root.clipboard_append(entry.get())
        root.update()
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
    history_frame.config(bg=bg)
    history_label.config(bg=bg, fg=fg)
    theme_btn.config(text="Dark Mode" if not is_dark_mode else "Light Mode")

    for btn in buttons:
        btn.config(bg=bg, fg=fg, activebackground="#444" if is_dark_mode else "#e6e6e6")

def update_history():
    history_text = "\n".join(history[-5:])  # Show last 5 entries
    history_var.set(history_text)

# Main window
root = tk.Tk()
root.title("Pro Calculator Plus")
root.geometry("400x600")
root.configure(bg="#f4f4f4")
root.bind("<Key>", key_press)

# Entry widget
entry = tk.Entry(root, font="Arial 20", bd=8, relief=tk.FLAT, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

# Theme toggle button
theme_btn = tk.Button(root, text="Dark Mode", command=toggle_theme, font=("Arial", 10), bg="#ffffff", relief=tk.GROOVE)
theme_btn.pack(pady=5)

# History section
history_frame = tk.Frame(root, bg="#f4f4f4")
history_frame.pack(fill="x", padx=10)
history_label = tk.Label(history_frame, text="History", font=("Arial", 12, "bold"), bg="#f4f4f4", anchor="w")
history_label.pack(anchor="w")
history_var = tk.StringVar()
history_display = tk.Label(history_frame, textvariable=history_var, justify="left", bg="#f4f4f4", font=("Consolas", 10))
history_display.pack(anchor="w")

# Buttons
button_layout = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"],
    ["(", ")", ".", "pi"],
    ["sin", "cos", "tan", "sqrt"],
    ["M+", "MR", "MC", "Copy"]
]

buttons = []
frame = tk.Frame(root, bg="#f4f4f4")
frame.pack()

for row in button_layout:
    button_row = tk.Frame(frame, bg="#f4f4f4")
    button_row.pack(expand=True, fill="both")
    for item in row:
        btn = tk.Button(button_row, text=item, font=("Arial", 14), bg="#ffffff", fg="#333333", relief=tk.GROOVE, borderwidth=1)
        btn.pack(side="left", expand=True, fill="both", padx=3, pady=3)
        btn.bind("<Button-1>", click)
        buttons.append(btn)

update_theme()
root.mainloop()
