
print("=======================")
print(" SIMPLE MENU ")
print("=======================")

 
while True:
    print()
    print("1 - Say Hello")
    print("2 - ShowMy Name")
    print("3 - Exit")

    
    choice = input("Select: ")

    if choice == "1":
       print("Hello")

    elif choice == "2":
        print("My name is Fahrettin.")

    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")

