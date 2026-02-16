 # main.py is the main code file that will use the functions defined in calc.py

import calc

while True:

    command = input("Enter command (add, sub, mult, div) or 'stop' to exit: ").lower()

    if command == "stop":
        print("Calculator stopped.")
        break

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if command == "add":
            result = calc.add(num1, num2)

        elif command == "sub":
            result = calc.subtract(num1, num2)

        elif command == "mult":
            result = calc.multiply(num1, num2)

        elif command == "div":
            result = calc.divide(num1, num2)

        else:
            print("Invalid command")
            continue

        print("Result:", result)

    except ValueError as e:
        print("Error:", e)

    except Exception:
        print("Invalid input. Please enter numbers only.")
