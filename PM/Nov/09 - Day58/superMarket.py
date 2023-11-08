import json
import csv

class Product:
    def __init__(self, name, price, quantity, category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.cart = []

    def add_to_cart(self, product, quantity):
        if product.quantity >= quantity:
            self.cart.append((product, quantity))
            product.quantity -= quantity
            return True
        else:
            print(f"Insufficient stock of {product.name}.")
            return False

    def remove_from_cart(self, product, quantity):
        for item in self.cart:
            if item[0] == product:
                if item[1] >= quantity:
                    item[1] -= quantity
                    product.quantity += quantity
                    if item[1] == 0:
                        self.cart.remove(item)
                    return True
                else:
                    print(f"Quantity exceeds what's in the cart.")
                    return False
        else:
            print(f"{product.name} not found in the cart.")
            return False

class Payment:
    def __init__(self, payment_method):
        self.payment_method = payment_method
        self.amount = 0

    def process_payment(self, amount):
        self.amount = amount
        print(f"Payment of Rs.{self.amount:.2f} using {self.payment_method} successful.")

class Supermarket:
    def __init__(self):
        self.inventory = []
        self.customers = {}

    def add_product(self, product):
        self.inventory.append(product)

    def add_customer(self, customer):
        if customer.name not in self.customers:
            self.customers[customer.name] = customer

    def remove_customer(self, customer):
        if customer.name in self.customers:
            del self.customers[customer.name]

    def display_products(self):
        print("Available Products:")
        for product in self.inventory:
            print(f"{product.name} - Rs.{product.price:.2f} ({product.quantity} available)")

    def calculate_bill(self, customer):
        total = sum(item[0].price * item[1] for item in customer.cart)
        return total


def load_products_from_file(supermarket, filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            for item in data:
                product = Product(item['name'], item['price'], item['quantity'], item['category'])
                supermarket.add_product(product)
    except FileNotFoundError:
        print("File not found.")

def load_products_from_csv(supermarket, filename):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                product = Product(
                    row['name'],
                    row['price'],
                    row['quantity'],
                    row['category']
                )
                supermarket.add_product(product)
    except FileNotFoundError:
        print("File not found.")

def main():
    supermarket = Supermarket()
    load_products_from_file(supermarket, 'products.json')  # Load products from a JSON file
    # load_products_from_csv(supermarket, 'products.csv')     # Load products from a CSV file

    while True:
        print("\n1. Add Customer")
        print("2. Add Product to Cart")
        print("3. Remove Product from Cart")
        print("4. Display Available Products")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter customer's name: ")
            balance = float(input("Enter customer's balance: "))
            customer = Customer(name, balance)
            supermarket.add_customer(customer)
            print(f"{name} has been added as a customer.")
        elif choice == '2':
            customer_name = input("Enter customer's name: ")
            if customer_name in supermarket.customers:
                customer = supermarket.customers[customer_name]
                supermarket.display_products()
                product_name = input("Enter product name: ")
                quantity = int(input("Enter quantity: "))
                for product in supermarket.inventory:
                    if product.name == product_name:
                        customer.add_to_cart(product, quantity)
                        break
                else:
                    print("Product not found.")
            else:
                print(f"Customer {customer_name} not found.")
        elif choice == '3':
            customer_name = input("Enter customer's name: ")
            if customer_name in supermarket.customers:
                customer = supermarket.customers[customer_name]
                supermarket.display_products()
                product_name = input("Enter product name: ")
                quantity = int(input("Enter quantity: "))
                for product in supermarket.inventory:
                    if product.name == product_name:
                        customer.remove_from_cart(product, quantity)
                        break
                else:
                    print("Product not found.")
            else:
                print(f"Customer {customer_name} not found.")
        elif choice == '4':
            supermarket.display_products()
        elif choice == '5':
            customer_name = input("Enter customer's name: ")
            if customer_name in supermarket.customers:
                customer = supermarket.customers[customer_name]
                total = supermarket.calculate_bill(customer)
                print(f"Total bill for {customer_name}: Rs.{total:.2f}")
                payment_method = input("Enter payment method (Cash/Card): ")
                payment = Payment(payment_method)
                payment.process_payment(total)
                del supermarket.customers[customer_name]  # Remove customer after checkout
            else:
                print(f"Customer {customer_name} not found.")
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
