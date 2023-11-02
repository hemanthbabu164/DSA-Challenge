import json

class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product ID: {self.product_id} - {self.name} - Price: ${self.price:.2f} - Available Quantity: {self.quantity}"

class Cart:
    def __init__(self):
        self.items = {}

    def add_to_cart(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id] += quantity
        else:
            self.items[product.product_id] = quantity

    def remove_from_cart(self, product, quantity):
        if product.product_id in self.items:
            if self.items[product.product_id] <= quantity:
                del self.items[product.product_id]
            else:
                self.items[product.product_id] -= quantity

    def get_total_price(self, products):
        total_price = 0
        for product_id, quantity in self.items.items():
            product = products[product_id]
            total_price += product.price * quantity
        return total_price

    def view_cart(self, products):
        if not self.items:
            print("Your cart is empty.")
            return

        print("Cart Contents:")
        for product_id, quantity in self.items.items():
            product = products[product_id]
            print(f"Product ID: {product.product_id} - {product.name} - Quantity in Cart: {quantity}")

def load_sample_data():
    with open('products.json', 'r') as jsonfile:
        products_data = json.load(jsonfile)
    
    products = {}
    for product_id, product_info in products_data.items():
        products[int(product_id)] = Product(int(product_id), product_info['name'], product_info['price'], product_info['quantity'])
    
    return products

def main():
    products = load_sample_data()
    cart = Cart()

    while True:
        print("\nFarming Product Ecommerce Emulation:")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nAvailable Products:")
            for product in products.values():
                print(product)
        elif choice == '2':
            product_id = int(input("Enter the Product ID to add to the cart: "))
            if product_id in products:
                quantity = int(input("Enter the quantity: "))
                if quantity <= products[product_id].quantity:
                    cart.add_to_cart(products[product_id], quantity)
                    products[product_id].quantity -= quantity
                    print(f"{quantity} {products[product_id].name} added to the cart.")
                else:
                    print("Insufficient quantity available.")
            else:
                print("Invalid Product ID.")
        elif choice == '3':
            product_id = int(input("Enter the Product ID to remove from the cart: "))
            if product_id in products:
                quantity = int(input("Enter the quantity to remove: "))
                cart.remove_from_cart(products[product_id], quantity)
                products[product_id].quantity += quantity
                print(f"{quantity} {products[product_id].name} removed from the cart.")
            else:
                print("Invalid Product ID.")
        elif choice == '4':
            cart.view_cart(products)
        elif choice == '5':
            total_price = cart.get_total_price(products)
            print(f"Total Price: ${total_price:.2f}")
            print("Thank you for shopping!")
            break
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
