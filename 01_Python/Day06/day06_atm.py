print ("============================")
print(" ATM LOGIN SYSTEM ")
print("=============================")

password = "1234"

attempt = 0

while attempt <3:

    user_password = input("Enter password: ")

    if user_password == password:
        print("Login Successful.")
        break

    else:
        print("Wrong Password.")
        attempt += 1

print()

if attempt ==3:
    print("Your card has been blocked.")