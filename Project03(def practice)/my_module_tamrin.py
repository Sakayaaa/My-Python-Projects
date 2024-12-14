import re

product_list = []


def get_info():
    name = input("Enter Product Name: ")
    price = int(input("Enter Product Price: "))
    quantity = int(input("Enter Product Quantity: "))
    payment_type = input("Enter Payment Type: ")

    return {"name": name, "price": price, "quantity": quantity, "payment_type": payment_type}


def price_check(price):
    if price > 0:
        return True
    else:
        print("Price must be greater than zero.")
        return False


def quantity_check(quantity):
    if quantity > 0:
        return True
    else:
        print("Quantity must be greater than zero.")
        return False


def payment_check(payment_type):
    if re.match(r"(cash)|(card)|(check)", payment_type):
        return True
    else:
        print("Payment type must be either cash, card or check.")
        return False


def product_list_print():
    n = 0
    for product in product_list:
        n = n + 1
        print(
            f"{n:^3}  |  Name: {product['name']:^10} | "
            f"Price: {product['quantity']:^3} x {product['price']:^8} ----> {product['quantity'] * product['price']:^8} | "
            f"Payment Type: {product['payment_type']:7}"
        )
        print("-"*100)


def total_print():
    total = 0

    for product in product_list:
        total = total + product['price'] * product['quantity']

    print(f"Total: {total:^8}")


def all_payment_print():
    cash = 0
    card = 0
    check = 0
    for product in product_list:
        if product['payment_type'] == 'cash':
            cash = cash + product['price'] * product['quantity']

        elif product['payment_type'] == 'card':
            card = card + product['price'] * product['quantity']

        elif product['payment_type'] == 'check':
            check = check + product['price'] * product['quantity']

    payment_dic = {"cash": cash, "card": card, "check": check}
    print(f"CASH: {payment_dic['cash']:^8}\nCARD: {payment_dic['card']:^8}\nCHECK: {payment_dic['check']:^8}")
