import re

pelak = input("Enter your pelak: ")

if re.match(r"\d{2}[آ-ی]\d{3}-iran|Iran\d{2}" , pelak):
    print("Your pelak is", pelak)
else:
    print("Invalid pelak!!!")