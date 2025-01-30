import tkinter as tk
from tkinter import messagebox, ttk  
from PIL import Image, ImageTk

class InventoryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("800x600")

        # Add a Canvas for the background image
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack()

        # Set the background image path
        background_image_path = "icons/Dashboard.gif"  # Adjust the path accordingly

        # Set the background image
        self.bg_image = Image.open(background_image_path)
        self.bg_image = self.bg_image.resize((800, 600))
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)

        # Initialize inventory data (using a dictionary for demonstration purposes)
        self.inventory = {"bedsheets": 100, "towels": 50, "pillow covers": 200, "soaps": 100, "room freshner": 100,
                          "hair dryers": 100}

        # Create widgets
        self.label_title = tk.Label(root, text="Inventory Management System", font=("Kozuka Gothic Pro B", 20),
                                    fg="white", bg="black")
        self.label_title.place(x=230, y=10)

        self.label_item = tk.Label(root, text="Item:", fg="white", bg="black", )
        self.label_item.place(x=150, y=150)
        self.entry_item = tk.Entry(root)
        self.entry_item.place(x=330, y=150)

        self.label_quantity = tk.Label(root, text="Quantity:", fg="white", bg="black")
        self.label_quantity.place(x=150, y=180)
        self.entry_quantity = tk.Entry(root)
        self.entry_quantity.place(x=330, y=180)

        self.label_select_item = tk.Label(root, text="Select Item to Update Quantity:", fg="white", bg="black")
        self.label_select_item.place(x=150, y=210)

        self.selected_item = tk.StringVar()  # Variable to store the selected item
        self.combo_item = ttk.Combobox(root, textvariable=self.selected_item, values=list(self.inventory.keys()))
        self.combo_item.place(x=330, y=210)

        self.btn_add_item = tk.Button(root, text="Add Item", command=self.add_item, bg="white", fg="black")
        self.btn_add_item.place(x=180, y=280)

        self.btn_update_quantity = tk.Button(root, text="Update Quantity", command=self.update_quantity, bg="white",
                                             fg="black")
        self.btn_update_quantity.place(x=260, y=280)

        self.btn_view_inventory = tk.Button(root, text="View Inventory", command=self.view_inventory, bg="white",
                                            fg="black")
        self.btn_view_inventory.place(x=370, y=280)

        # Display area for inventory
        self.label_inventory = tk.Label(root, text="", font=("Courier", 12), anchor="w", justify="left", bg="white",
                                        fg="black")
        self.label_inventory.place(x=200, y=420, anchor="w")

    def add_item(self):
        item = self.entry_item.get()
        quantity = self.entry_quantity.get()

        if not item or not quantity.isdigit():
            messagebox.showwarning("Warning", "Please enter a valid item and quantity.")
            return

        quantity = int(quantity)

        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

        messagebox.showinfo("Success", f"Item '{item}' added successfully.")
        self.update_inventory_label()
        self.update_combo_values()

    def update_quantity(self):
        item = self.selected_item.get()
        quantity = self.entry_quantity.get()

        if not item or not quantity.isdigit():
            messagebox.showwarning("Warning", "Please enter valid item and quantity.")
            return

        quantity = int(quantity)

        if item in self.inventory:
            self.inventory[item] = quantity
            messagebox.showinfo("Success", f"Quantity for item '{item}' updated successfully.")
            self.update_inventory_label()
        else:
            messagebox.showwarning("Warning", f"Item '{item}' not found in inventory.")

    def view_inventory(self):
        self.update_inventory_label()

    def update_inventory_label(self):
        inventory_text = "Current Inventory:\n"
        for item, quantity in self.inventory.items():
            inventory_text += f"{item}: {quantity}\n"
        self.label_inventory.config(text=inventory_text)

    def update_combo_values(self):
        # Update ComboBox values with the current inventory items
        self.combo_item['values'] = list(self.inventory.keys())


if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryManagementSystem(root)
    root.mainloop()
