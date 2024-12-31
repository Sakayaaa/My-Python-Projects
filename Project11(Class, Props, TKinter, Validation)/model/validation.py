import re
from datetime import datetime


# NAME VALIDATION
def name_validator(name):
    if type(name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", name):
        return name
    else:
        raise ValueError("Invalid Name !!!")


# CODE VALIDATION
def code_validator(code):
    if type(code) == str and re.match(r"^\d{3}$", code):
        return code
    else:
        raise ValueError("Invalid Code !!!")


# DAY OF THE WEEK VALIDATION
def day_validator(day):
    day = day.lower()
    if type(day) == str and day in ["shanbe", "yekshanbe", "doshanbe", "seshanbe", "charshanbe", "panjshanbe"]:
        return day
    else:
        raise ValueError("Invalid Day !!!")


# CLASS DURATION VALIDATION
def duration_validator(duration):
    try:
        new_duration = int(duration)
        if type(new_duration) == int and 60 <= new_duration <= 180:
            return new_duration
        else:
            raise ValueError("Invalid Duration !!!")
    except:
        raise ValueError("Duration Must Be INT !!!")


# TEACHER NAME VALIDATION
def teacher_validator(teacher):
    if type(teacher) == str and re.match(r"^[a-zA-Z\s]{3,30}$", teacher):
        return teacher
    else:
        raise ValueError("Invalid Teacher Name !!!")


# CLASS STARTING TIME VALIDATION
def time_validator(start_time):
    try:
        if type(start_time) == str:
            return datetime.strptime(start_time, "%H:%M").time()
    except:
        raise ValueError("Invalid Time !!!")
