def calculator():
    while True:
        try:
            # Get user input for the numbers
            num1_input = input("Enter the first number (or 'q' to quit): ")
            if num1_input.lower() == 'q':
                break
            num1 = float(num1_input)
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
            while True:
                try:
                    choice = int(input("Enter your choice (1-7): "))
                    if choice < 1 or choice > 7:
                        raise ValueError("Invalid choice. Please enter a number from 1 to 7.")
                    break
                except ValueError as e:
                    print(e)

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

        except ValueError:
            print("Error: Please enter numeric values.")

        # Ask if the user wants to continue or quit
        while True:
            choice = input("Do you want to continue (y/n)? ").lower()
            if choice == 'y' or choice == 'n':
                break
            else:
                print("Invalid choice. Please enter 'y' or 'n'.")

        if choice == 'n':
            break


calculator()
