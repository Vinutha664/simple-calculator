def calculator():
    print("===== Simple Calculator =====")
    print("Supported operations: +  -  *  /  %  //  **")
    print("Type 'exit' anytime to close the calculator.\n")

    while True:
        try:
            num1 = input("Enter first number (or 'exit' to quit): ").strip()
            if num1.lower() == 'exit':
                print("Calculator exited.")
                break
            num1 = float(num1)

            operator = input("Enter operator (+, -, , /, %, //, *): ").strip()
            if operator.lower() == 'exit':
                print("Calculator exited.")
                break
            if operator not in ['+', '-', '', '/', '%', '//', '*']:
                print("Invalid operator. Try again.\n")
                continue

            num2 = input("Enter second number: ").strip()
            if num2.lower() == 'exit':
                print("Calculator exited.")
                break
            num2 = float(num2)

            # Perform calculation
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.\n")
                    continue
                result = num1 / num2
            elif operator == '%':
                result = num1 % num2
            elif operator == '//':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.\n")
                    continue
                result = num1 // num2
            elif operator == '**':
                result = num1 ** num2

            print(f"Result: {result}\n")

        except ValueError:
            print("Invalid number input. Please try again.\n")

calculator()