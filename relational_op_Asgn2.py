# write a python to determine grade of the student
# A: score>=90
# B: score>=80 and score<90
# c: score>=70 and score<80
# D: score>=60 and score<70
# E: score<60


import tkinter as tk
from tkinter import messagebox


def calculate_grade():
    try:
        score = float(entry.get())  # Get score from input field
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "E"

        result_label.config(text=f"Grade: {grade}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid score")


# Create the main window
root = tk.Tk()
root.title("Student Grade Calculator")

# Create and place widgets
tk.Label(root, text="Enter Student Score:").pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

calculate_button = tk.Button(root, text="Calculate Grade", command=calculate_grade)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the main event loop
root.mainloop()

# write a python program to calculate a discount for a customer  based on the purchase using tkinter
# conditions:
'''purchase>=$500: 20% discount
purchase>=200 and <$500: 10% discount
purchase=int(e1.get())'''
import tkinter as tk
from tkinter import messagebox

def calculate_discount():
    try:
        customer_purchase = int(e1.get())
        if customer_purchase >= 500:
            discount = 0.2
        elif customer_purchase >= 200:
            discount = 0.1
        else:
            discount = 0.0

        amt_to_be_paid = customer_purchase - (customer_purchase * discount)

        # Display the result in a message box
        messagebox.showinfo("Total Amount to be Paid", f"Total Amount: ${amt_to_be_paid:.2f}\nDiscount: {discount * 100}%")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer amount.")

# Create the main window
root = tk.Tk()
root.title("Discount Calculator")

# Create and place the input field
tk.Label(root, text="Enter Purchase Amount:").pack(pady=10)
e1 = tk.Entry(root)
e1.pack(pady=10)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate Discount", command=calculate_discount)
calculate_button.pack(pady=20)

# Run the application
root.mainloop()
