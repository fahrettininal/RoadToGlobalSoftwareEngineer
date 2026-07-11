print("============================")
print("DAY05 CHALLENGEV2")
print("============================")

salary = int(input("Maaşınız:"))

print()

if salary >= 90000:
    print("Principal Developer")

elif salary >= 70000 and salary <= 89999:
    print("Senior Developer")

elif salary >= 50000 and salary <= 69999:
    print("Mid Developer")

elif salary >= 45000 and salary <= 49999:
    print("Junior Developer")

else:
    print("Intern")