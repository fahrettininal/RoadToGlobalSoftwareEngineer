print("============================")
print(" EMPLYEE SYSTEM ")
print("============================")

age =int(input("Age: "))
salary = int(input("Salary:"))
experience = int(input("Years of experience: "))

print()

if age >= 18 and salary >= 45000 and experience >= 2:
    print("Congratulations!")
    print("You are eligible.")

else:
    print("Sorry!")
    print("You are not eligible.")
            
