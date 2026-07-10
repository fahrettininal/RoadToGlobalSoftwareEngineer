

print("===============================")
print(" OR OPERATOR ")
print("===============================")

role = input("Enter your role(staff/admin/guest): ")

print()

if role == "staff" or role == "admin":
    print("You have access to the system.")
    print("Access granted.")
else:
    print("Access denied.")



print("===============================")
print(" LOGIN SYSTEM ")
print("===============================")

username = input("Username: ")

print()

if username == "Fahrettin" or username == "Admin":
    print("Login successfull.")
else:
    print("Unknown user.")

