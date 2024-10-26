from tkinter import *
from tkinter import messagebox

def check_discount():
    try:
        purchase_amt = float(e1.get())  # Get purchase amount from entry
        membership = var.get()  # Get membership status from radio buttons

        if purchase_amt > 5000 or membership:
            discount = purchase_amt * 0.20
            messagebox.showinfo("Discount Eligibility", f"Eligible for 20% discount: {discount:.2f}")
        else:
            messagebox.showinfo("Discount Eligibility", "Not eligible for discount.")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for purchase amount.")

# Create main window
window3 = Tk()
window3.title("Discount Eligibility Checker")
window3.configure(background='#FFC0CB')  # Set background color to pink

# Label for application name
Label(window3, text="Discount Eligibility Checker", font=("Arial", 16, "bold"), bg='#FFC0CB').grid(row=0, column=0, columnspan=2, pady=10)

# Entry for purchase amount
Label(window3, text="Enter Purchase Amount:", bg='#FFC0CB').grid(row=1, column=0, padx=10, pady=10)
e1 = Entry(window3)
e1.grid(row=1, column=1, padx=10, pady=10)

# Radio buttons for membership status
var = BooleanVar()
var.set(False)  # Default value

Label(window3, text="Membership Status:", bg='#FFC0CB').grid(row=2, column=0, padx=10, pady=10)
Radiobutton(window3, text="Yes", variable=var, value=True, bg='#FFC0CB').grid(row=2, column=1, sticky='w')
Radiobutton(window3, text="No", variable=var, value=False, bg='#FFC0CB').grid(row=2, column=1, sticky='e')

# Button to check discount eligibility
btn_check_discount = Button(window3, text="Check Discount", command=check_discount, bg='#FFC0CB', fg='white')
btn_check_discount.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
window3.mainloop()