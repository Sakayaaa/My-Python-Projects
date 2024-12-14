import re

coef_list = []

while input("Do you want to add a lesson? (y/n): ").lower() == "y":
    name = input("Enter lesson's name: ")
    if re.match(r"^[a-zA-Z0-9\s]{3,30}$" , name):
        coef = int(input("Enter lesson's coef: "))
        if coef in (1, 2, 3, 5):

            if sum(coef_list) + coef <= 17:
                coef_list.append(coef)
            else:
                print("Your lessons are Full!!!")
        else:
            print("Invalid coef!!!")
    else:
        print("Invalid name!!!")

print("Your coef list is:", coef_list)
print("Your coef sum is:" , sum(coef_list))