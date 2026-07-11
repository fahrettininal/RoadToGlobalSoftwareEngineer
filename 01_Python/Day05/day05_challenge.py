print("===========================")
print(" DAY05 CHALLANGE ")
print("=============================")

name = input("Adiniz:")
age = int(input("Yasiniz:"))
salary = int(input("Maasiniz:"))


if age >= 18 and salary >= 45000 and (name == "Fahrettin" or name == "Admin"):

    print("Access Granted")

else:
    print("Access Denied")