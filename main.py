def calculator():
    while True:
        try:
            # Get user input for the numbers
            num1 = float(input("Enter the first number (or 'q' to quit): "))
            if num1 == 'q':
                break
            num2 = float(input("Enter the second number: "))

            # Display operation menu
            print("Select an operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exponentiation")
            print("6. Floor Division")
            print("7. Modulus")

            # Get user input for the operation choice
            choice = int(input("Enter your choice (1-7): "))

            # Perform the selected operation and print the result
            if choice == 1:
                result = num1 + num2
                print(f"The result of {num1} + {num2} is {result}")
            elif choice == 2:
                result = num1 - num2
                print(f"The result of {num1} - {num2} is {result}")
            elif choice == 3:
                result = num1 * num2
                print(f"The result of {num1} * {num2} is {result}")
            elif choice == 4:
                try:
                    result = num1 / num2
                    print(f"The result of {num1} / {num2} is {result}")
                except ZeroDivisionError:
                    print("Error: Division by zero is not allowed.")
            elif choice == 5:
                result = num1 ** num2
                print(f"The result of {num1} ** {num2} is {result}")
            elif choice == 6:
                try:
                    result = num1 // num2
                    print(f"The result of {num1} // {num2} is {result}")
                except ZeroDivisionError:
                    print("Error: Division by zero is not allowed.")
            elif choice == 7:
                try:
                    result = num1 % num2
                    print(f"The result of {num1} % {num2} is {result}")
                except ZeroDivisionError:
                    print("Error: Division by zero is not allowed.")
            else:
                print("Invalid choice. Please enter a number from 1 to 7.")

        except ValueError:
            print("Error: Please enter numeric values.")

        # Ask if the user wants to continue or quit
        choice = input("Do you want to continue (y/n)? ").lower()
        if choice != 'y':
            break


calculator()
