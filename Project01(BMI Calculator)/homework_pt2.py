Weight = float(input("Enter Your Weight in Kg: "))

Height = float(input("Enter Your Height in Cm: "))
Height = Height / 100

BMI = round(Weight / (Height**2), 2)
print("Your BMI is:", BMI)

if BMI < 18.5:
    print("You are underweight!!!")

elif 18.5 <= BMI < 25:
    print("You are normal!!!")

else:
    print("Lose some weight!!!")


