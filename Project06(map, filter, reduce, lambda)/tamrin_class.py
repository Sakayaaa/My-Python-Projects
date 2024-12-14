from functools import reduce

student_list = [
    {"name":"ali" , "vahed":3 , "ostad":"mesbah"},
    {"name":"reza" , "vahed":5 , "ostad":"moradi"},
    {"name":"hosein" , "vahed":2 , "ostad":"ahmadi"},
    {"name":"saeed" , "vahed":2 , "ostad":"asghari"},
    {"name":"amir" , "vahed":1 , "ostad":"jafari"}
]


vahed_balaye_3= list(filter(lambda  std:std["vahed"]>=3, student_list))
print("Upper 3 Unit :",vahed_balaye_3)

vahedha = list(map(lambda std : std["vahed"], student_list))
majmoe_vahed = reduce(lambda a,b:a+b, vahedha)
print(f'Majmoe Vahed ha: {majmoe_vahed}')

print("-"*50)
hazine = 2000

hazine_x_vahed = list(map(lambda std:std["vahed"] * hazine, student_list))
print(f"List hazine ha: {hazine_x_vahed}")

print("-"*50)

majmoe_hazine = reduce(lambda a,b:a+b, hazine_x_vahed)
print(f"Majmoe Hazine ha: {majmoe_hazine}")
