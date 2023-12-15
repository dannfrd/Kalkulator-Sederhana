# uas_[nim].py
import tkinter as tk
from tkinter import messagebox
from Librarymu import calculator_class

def main():
    # Create a Calculator object
    calculator = calculator_class.Calculator()

    # Tkinter GUI setup
    root = tk.Tk()
    root.title("Simple Calculator")

    # Entry widget to display the current expression
    entry = tk.Entry(root, width=20, font=("Arial", 16), bd=5, insertwidth=4, justify='right')
    entry.grid(row=0, column=0, columnspan=4)

    # Function to update the expression in the entry widget
    def update_expression(value):
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text + str(value))

    # Function to evaluate the expression
    def evaluate_expression():
        try:
            result = calculator.evaluate(entry.get())
            entry.delete(0, tk.END)
            
            # Check if the result is not None before displaying
            if result is not None:
                entry.insert(tk.END, str(result))
            else:
                messagebox.showerror("Error", "Invalid expression")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # Function to perform addition
    def perform_addition():
        update_expression('+')

    # Function to perform subtraction
    def perform_subtraction():
        update_expression('-')

    # Function to perform multiplication
    def perform_multiplication():
        update_expression('*')

    # Function to perform division
    def perform_division():
        update_expression('/')

    # Buttons for numbers and operations
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
        ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3),
    ]

    # Create and place buttons in the grid
    for (text, row, col) in buttons:
        if text == '=':
            button = tk.Button(root, text=text, padx=20, pady=20, command=evaluate_expression)
        elif text == 'C':
            button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: entry.delete(0, tk.END))
        elif text in {'+', '-', '*', '/'}:
            button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: update_expression(t))
        else:
            button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: update_expression(t))
        button.grid(row=row, column=col)

    # Run the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
