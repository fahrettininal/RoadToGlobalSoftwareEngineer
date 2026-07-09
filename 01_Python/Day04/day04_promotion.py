print("===============================")
print("PROMOTTION SYSTEM")
print("===============================")

name = input("Enter your name:")
salary = int(input("Enter your salary:"))

if salary >= 700000:
    print("Hello", name)
    print("Position: Senior Developer")

elif salary >= 45000 and salary <= 69999:
    print("Hello", name)
    print("Position: Mid Developer")

else:
    print("Hello", name)
    print("Position: Junior Developer")



