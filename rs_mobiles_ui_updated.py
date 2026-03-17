# Modernized and Refactored UI for Billing System Application

import tkinter as tk
from tkinter import messagebox

class BillingSystemUI:
    def __init__(self, master):
        self.master = master
        self.master.title('Billing System')
        self.master.geometry('800x600')
        self.create_widgets()

    def create_widgets(self):
        # Header
        self.header = tk.Label(self.master, text='Billing System', font=('Arial', 24))
        self.header.pack(pady=20)

        # Customer Information
        self.customer_frame = tk.Frame(self.master)
        self.customer_frame.pack(pady=10)

        tk.Label(self.customer_frame, text='Customer Name:').grid(row=0, column=0)
        self.customer_name = tk.Entry(self.customer_frame)
        self.customer_name.grid(row=0, column=1)

        tk.Label(self.customer_frame, text='Customer ID:').grid(row=1, column=0)
        self.customer_id = tk.Entry(self.customer_frame)
        self.customer_id.grid(row=1, column=1)

        # Billing Information
        self.billing_frame = tk.Frame(self.master)
        self.billing_frame.pack(pady=20)

        tk.Label(self.billing_frame, text='Total Amount:').grid(row=0, column=0)
        self.total_amount = tk.Entry(self.billing_frame)
        self.total_amount.grid(row=0, column=1)

        tk.Button(self.billing_frame, text='Generate Bill', command=self.generate_bill).grid(row=1, columnspan=2, pady=10)

    def generate_bill(self):
        name = self.customer_name.get()
        customer_id = self.customer_id.get()
        total = self.total_amount.get()
        if name and customer_id and total:
            messagebox.showinfo('Bill Generated', f'Bill for {name} (ID: {customer_id}) has been generated successfully! Total: ${total}')
        else:
            messagebox.showwarning('Input Error', 'Please fill in all fields.')

if __name__ == '__main__':
    root = tk.Tk()
    app = BillingSystemUI(master=root)
    root.mainloop()