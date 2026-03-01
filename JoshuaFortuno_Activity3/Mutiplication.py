def multiply_numbers():
    io = False

    while True:
        if not io:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            result = num1 * num2
            print("Product:", result)

        ta = str(input("\nTry again? (y/n): "))

        if ta.strip().lower() == "y":
            io = False
            continue
        elif ta.strip().lower() == "n":
            break
        else:
            io = True
            print("Invalid option.")

multiply_numbers()