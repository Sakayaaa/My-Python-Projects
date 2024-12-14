import re

# PRODUCTS
total = 0
products = []

while input("Do you want to add a product? (y/n): ").lower() == "y":
    name = input("Enter a product name: ")
    if re.match(r"^[a-zA-Z0-9\s]{1,30}$", name):
        quantity = int(input("Enter a product quantity: "))
        price = int(input("Enter a product price: "))
        if quantity > 0 and price > 0:
            total = total + (quantity * price)
            product = {"Product Name": name, "Product Quantity": quantity, "Product Price": price}
            products.append(product)
        else:
            print("Quantity and Price must be greater than zero!!!")
    else:
        print("Invalid product name!!!")

print("Products added:")
for product in products:
    print(product)

print("Your total cost is: ", total)
