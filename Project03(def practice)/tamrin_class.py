from my_module_tamrin import *

while input("Add Product? (y/n): ").lower() == "y":
#GET DATA
    product = get_info()

    print("-" * 50)
#DATA VALIDATION
    if price_check(product["price"]) and quantity_check(product["quantity"]) and payment_check(product["payment_type"]):
        product_list.append(product)
else:
    print("-" * 100)

#PRODUCTS PRINT IN LIST
product_list_print()

#TOTAL PRICE PRINT
total_print()

print("-"*50)

#PRINT EACH PAYMENT METHOD TOTAL PRICE
all_payment_print()
