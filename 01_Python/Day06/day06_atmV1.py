
print("======================")
print(" ATM SYSTEM ")
print("======================")

balance = 500

while True:
    print()
    print("1 - Show Balance : ")
    print("2 - Deposit Money : ")
    print("3 - withdraw Money : ")
    print("4 - Exit : ")
    
    choice = input("Select: ")

    if choice == "1":
        print()
        print("Your balance:", balance, "TL")

    elif choice == "2":

        amount = int(input("Enter amount: "))

        balance = balance + amount

        print()
        print("Money deposited successfully.")
        print("New balance:", balance, "TL")

    elif choice == "3":
        amount =int(input("Enter Amount: "))

        if amount <= balance:
            balance = balance - amount

            print()
            print("Money withdrawn successfully.")
            print("New balance:", balance, "TL")

        else:
            print()
            print("Insufficient Balance!")

    elif choice == "4":
        print()
        print("Thank you for using our ATM.")
        print("Goodbye!")

    else:
        print()
        print("Invalid selection!")

