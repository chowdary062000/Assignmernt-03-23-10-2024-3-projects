import tkinter as tk


class InventoryManagementSystem:
    def __init__(self):
        self.window = tk.Tk()  # Create the main window
        self.window.title("Inventory Management System")

        # Inventory structure: a list of dictionaries
        self.inventory_product = [
            {"name": "Laptops", "quantity": 10, "sold_on_amazon": True},
            {"name": "Smart Watches", "quantity": 5, "sold_on_amazon": True},
            {"name": "Smart Phones", "quantity": 15, "sold_on_amazon": False},
            {"name": "Earbuds", "quantity": 20, "sold_on_amazon": True},
            {"name": "Tablet", "quantity": 8, "sold_on_amazon": False},
            {"name": "Camera", "quantity": 3, "sold_on_amazon": True}
        ]

        # Create a Label and entry field for searching products
        self.search_Label = tk.Label(self.window, text="Enter the product you want to search:")
        self.search_Label.pack()
        self.search_Entry = tk.Entry(self.window)
        self.search_Entry.pack()

        # Create a button to start the search
        self.search_buttons = tk.Button(self.window, text="Search", command=self.search_product)
        self.search_buttons.pack()

        # Create a text box to display the search results
        self.result_text = tk.Text(self.window, height=10, width=40)
        self.result_text.pack()

    def search_product(self):
        search_query = self.search_Entry.get().lower()  # Get the search query
        found = False  # Flag to check if product is found
        for product in self.inventory_product:
            if product["name"].lower() == search_query:  # Check if product matches
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END, f"Product: '{product['name']}'\n")
                self.result_text.insert(tk.END, f"Quantity: {product['quantity']}\n")
                self.result_text.insert(tk.END, f"Sold on Amazon: {'Yes' if product['sold_on_amazon'] else 'No'}")
                found = True
                break  # Exit the loop if product is found

        # Display a message if the product is not found
        if not found:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, "Product not found in inventory.")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    system = InventoryManagementSystem()
    system.run()