print("===========================")
print(" EMPLOYEE PROMOTION ")
print("===========================")

salary = int(input("Salary:"))

print()

if salary >= 45000:

    print("Salary requirement passed.")

    if salary >= 70000:
        print("Promotion: Senior Developer")

    else:
        print("Pronotion: Mid Developer")

else:
    print("Promotion: Junior Developer")
    
