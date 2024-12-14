import re
import tkinter.messagebox as msg


def name_validator(name):
    return bool(re.match(r"^[a-zA-Z\s]{2,30}$", name))

def price_validator(price):
    return price > 0


def quantity_validator(quantity):
    return quantity > 0