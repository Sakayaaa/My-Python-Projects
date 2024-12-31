import re
from datetime import datetime


def name_validator(name):
    if type(name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", name):
        return name
    else:
        raise ValueError("Invalid Name !!!")


def grade_validator(grade):
    if type(grade) == int and grade in [1, 2, 3]:
        return grade
    else:
        raise ValueError("Invalid grade !!!")


def license_date_validator(license_date):
    try:
        if type(license_date) == str:
            return datetime.strptime(license_date, "%Y-%m-%d")
    except:
        raise ValueError("Invalid Date !!!")


def license_no_validator(license_no):
    if type(license_no) == str and re.match(r"^\d{10}$", license_no):
        return license_no
    else:
        raise ValueError("Invalid License No. !!!")