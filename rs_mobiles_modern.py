import tkinter as tk
from tkinter import messagebox

class BillingSystem:
    def __init__(self, master):
        self.master = master
        master.title('Modern Billing System')

        # Create the login window
        self.login_frame = tk.Frame(master)
        self.login_frame.pack()
        self.username_label = tk.Label(self.login_frame, text='Username:')
        self.username_label.pack()
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()
        self.login_button = tk.Button(self.login_frame, text='Login', command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        if username:
            messagebox.showinfo('Welcome', f'Logged in as {username}')
            self.login_frame.pack_forget()
            self.show_dashboard()
        else:
            messagebox.showwarning('Login Failed', 'Please enter a username.')

    def show_dashboard(self):
        # Create the dashboard layout
        self.dashboard_frame = tk.Frame(self.master)
        self.dashboard_frame.pack()

        # Add a sidebar
        self.sidebar = tk.Frame(self.dashboard_frame, width=200, bg='lightgray')
        self.sidebar.pack(side='left', fill='y')

        self.main_area = tk.Frame(self.dashboard_frame, bg='white')
        self.main_area.pack(side='right', fill='both', expand=True)

        self.sidebar_title = tk.Label(self.sidebar, text='Dashboard Menu')
        self.sidebar_title.pack(pady=10)
        self.bill_button = tk.Button(self.sidebar, text='Create Bill', command=self.create_bill)
        self.bill_button.pack(pady=5)
        self.product_button = tk.Button(self.sidebar, text='Product Management', command=self.manage_products)
        self.product_button.pack(pady=5)
        self.customer_button = tk.Button(self.sidebar, text='Customer Management', command=self.manage_customers)
        self.customer_button.pack(pady=5)
        self.report_button = tk.Button(self.sidebar, text='Stock Reports', command=self.show_reports)
        self.report_button.pack(pady=5)
        self.supplier_button = tk.Button(self.sidebar, text='Supplier Management', command=self.manage_suppliers)
        self.supplier_button.pack(pady=5)

    def create_bill(self):
        # Implement bill creation window
        pass

    def manage_products(self):
        # Implement product management window
        pass

    def manage_customers(self):
        # Implement customer management window
        pass

    def show_reports(self):
        # Implement stock reports window
        pass

    def manage_suppliers(self):
        # Implement supplier management window
        pass

if __name__ == '__main__':
    root = tk.Tk()
    billing_system = BillingSystem(root)
    root.mainloop()