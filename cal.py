import tkinter as tk
import math
import cmath

def button_click(value):
    if value == '+/-':
        negate()
    elif value == 'x^2':
        try:
            result = float(entry.get()) ** 2
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == '√':
        sqrt()
    elif value == '%':
        percentage()
    else:
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

def sqrt():
    try:
        value = float(entry.get())
        if value < 0:
            result = cmath.sqrt(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        else:
            result = math.sqrt(value)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Invalid input")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: " + str(e))

def percentage():
    try:
        result = float(entry.get()) / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Invalid input")
    except ZeroDivisionError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Cannot divide by zero")
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: " + str(e))

def negate():
    try:
        current_value = entry.get()
        if current_value.startswith('-'):
            result = float(current_value[1:])
        else:
            result = -float(current_value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def evaluate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, f"Error: {str(e)}")

root = tk.Tk()
root.title("Colorful Calculator")
root.geometry("360x500")
root.config(bg="#280c35")

entry = tk.Entry(root, width=20, font=('Bell MT', 20), justify=tk.RIGHT, bd=10)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=19)

buttons = ['7', '8', '9', '+/-', '4', '5', '6', '/', '1', '2', '3', '*', '0', '.', '=', '+', 'x^2', '√', '%', '-']

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=19, pady=19, font=('Bell MT', 15, 'bold'), command=lambda b=button: button_click(b) if b != '=' else evaluate(), bg="#8B8000", fg="#a7b5bb").grid(row=row_val, column=col_val, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text='C', padx=20, pady=20, font=('Bell MT', 15, 'bold'), command=clear_entry, bg="#27444d", fg="#366755").grid(row=row_val, column=0, sticky="nsew")
tk.Button(root, text='←', padx=20, pady=20, font=('Bell MT', 15), command=backspace, bg="#27444d", fg="#366755").grid(row=row_val, column=1, sticky="nsew")

for i in range(1, 6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i-1, weight=1)

root.mainloop()
