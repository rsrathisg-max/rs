# Full Modernized Billing System Code

## Features
- Billing
- Inventory Management
- Customers Management
- Suppliers Management
- Reporting

## Billing Module
class Billing:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, item, price):
        self.items.append({'item': item, 'price': price})
        self.total += price

    def calculate_total(self):
        return self.total

## Inventory Module
class Inventory:
    def __init__(self):
        self.stock = {}

    def add_product(self, product, quantity):
        self.stock[product] = self.stock.get(product, 0) + quantity

    def reduce_stock(self, product, quantity):
        if product in self.stock:
            self.stock[product] -= quantity

## Customers Module
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

## Suppliers Module
class Supplier:
    def __init__(self, name, contact):
        self.name = name
        self.contact = contact

## Reporting Module
class Reports:
    def generate_billing_report(self, bills):
        # Logic for generating billing reports
        return bills

# Example of utilization:
billing = Billing()
billing.add_item('Product A', 50)
billing.add_item('Product B', 30)

print('Total:', billing.calculate_total())
