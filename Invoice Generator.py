# Invoice Generator

class Invoice:
    def __init__(self, company_name, company_address, invoice_number, date, bill_to, ship_to):
        self.company_name = company_name
        self.company_address = company_address
        self.invoice_number = invoice_number
        self.date = date
        self.bill_to = bill_to
        self.ship_to = ship_to
        self.items = []

    def add_item(self, item_name, quantity, price):
        self.items.append({"item_name": item_name, "quantity": quantity, "price": price})

    def generate_invoice(self):
        print("Invoice #", self.invoice_number)
        print("Date:", self.date)
        print("Bill To:", self.bill_to)
        print("Ship To:", self.ship_to)
        print("")

        print("Items:")
        for item in self.items:
            print(f"{item['item_name']}: {item['quantity']} x Rs{item['price']} = Rs{item['quantity'] * item['price']:.2f}")
        print("")

        total = sum(item['quantity'] * item['price'] for item in self.items)
        print("Total:", f"Rs{total:.2f}")

def main():
    company_name = input("Enter company name: ")
    company_address = input("Enter company address: ")
    invoice_number = input("Enter invoice number: ")
    date = input("Enter date (YYYY-MM-DD): ")
    bill_to = input("Enter bill to: ")
    ship_to = input("Enter ship to: ")

    invoice = Invoice(company_name, company_address, invoice_number, date, bill_to, ship_to)

    while True:
        item_name = input("Enter item name (or 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        invoice.add_item(item_name, quantity, price)

    invoice.generate_invoice()

if __name__ == "__main__":
    main()

