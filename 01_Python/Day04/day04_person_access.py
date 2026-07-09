print("================================")
print(" PERSON ACCESS SYSTEM ")
print("================================")

name = input("Enter your name:")
age = int(input("Enter your age:"))

print

if age >= 18:
    print("Welcome,", name)
    print("Access granted.")

else:
    print("Sorry,", name)
    print("Access denied.")
