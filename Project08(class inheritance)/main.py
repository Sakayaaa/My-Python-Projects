    #Import Section
from laptop import Laptop
from mobile import Mobile
from speaker import Speaker
from furniture import Furniture


    #Main Section
#Laptop
laptop_1 = Laptop()
laptop_1.name = input("Enter Laptop Name: ")
laptop_1.price = input("Enter Laptop Price: ")
laptop_1.voltage = input("Enter Laptop Voltage: ")
laptop_1.ram = input("Enter Laptop Ram: ")
laptop_1.cpu = input("Enter Laptop CPU: ")
print(laptop_1)

#Mobile
mobile_1 = Mobile()
mobile_1.name = input("Enter Mobile Name: ")
mobile_1.price = input("Enter Mobile Price: ")
mobile_1.voltage = input("Enter Mobile Voltage: ")
mobile_1.screen_size = input("Enter Mobile Screen Size: ")
print(mobile_1)

#Speaker
speaker_1 = Speaker()
speaker_1.name = input("Enter Speaker Name: ")
speaker_1.price = input("Enter Speaker Price: ")
speaker_1.voltage = input("Enter Speaker Voltage: ")
speaker_1.power = input("Enter Speaker Power: ")
print(speaker_1)

#Furniture
furniture_1 = Furniture()
furniture_1.name = input("Enter Furniture Name: ")
furniture_1.price = input("Enter Furniture Price: ")
furniture_1.weight = input("Enter Furniture Weight: ")
furniture_1.capacity = input("Enter Furniture Capacity: ")
print(furniture_1)
