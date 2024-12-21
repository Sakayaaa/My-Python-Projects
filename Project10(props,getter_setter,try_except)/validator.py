import re


def title_validator(title):
    if title in ["card", "savings", "credit"]:
        return title
    else:
        raise ValueError("Invalid Title")


def account_id_validator(account_id):
    if re.match(r"^6104[0-9]{12}$" , account_id):
        return account_id
    else:
        raise ValueError("Invalid Account ID")


def amount_validator(amount):
    try:
        new_amount = int(amount)
    except ValueError:
        raise ValueError("You Must Enter An Integer")

    if new_amount >= 0:
        return new_amount
    else:
        raise ValueError("Invalid Amount")

