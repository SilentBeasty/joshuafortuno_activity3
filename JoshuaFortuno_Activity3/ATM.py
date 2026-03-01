def atm():
    sb = type(False)
    balance = 1000

    while True:
        print("\n+-----[ ATM MENU ]-----+")
        print("| 1. Check Balance     |")
        print("| 2. Deposit           |")
        print("| 3. Withdraw          |")
        print("| 4. Exit              |")
        print("+----------------------+")

        if sb == True:
            print("Current Balance:", balance)
            sb = False

        choice = input("Choose option: ")

        if choice == "1":
            sb = True

        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            if amount >= 1:
                amount += amount
                print("Deposit successful.")
            else:
                print("Input a valid number.")

        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            if amount <= balance:
                if amount >= 1:
                    balance -= amount
                    print("Withdrawal successful.")
                else:
                    print("Input a valid number.")
            else:
                print("Insufficient balance.")

        elif choice == "4":
            print("Thank you for using ATM.")
            break

        else:
            print("Invalid option.")

atm()