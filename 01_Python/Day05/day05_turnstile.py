print("======================")
print(" TURNSTİLE ")
print("===========================")

name = input("Enter your name:")
age =  int(input("Enter your age:"))
cart = input("Enter your card (yes/no):")
personel = input("Are you personel? (yes/no):")


print()

if name == "Fahrettin" and age >= 18 and cart == "yes" and personel == "yes":
    print("Turnstille Opened")
    print("Welcome Fahrettin")


else:
    print("Turnstile Locked")
    print("Access Denied")

