import os

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def modulus(x, y):
    return x % y

def exponentiate(x, y):
    return x ** y

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator():
    history = []

    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Exponentiation")
        print("7. Show History")
        print("8. Clear Screen")
        print("9. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7/8/9): ")

        if choice == '9':
            print("Exiting the calculator. Goodbye!")
            break

        if choice == '7':
            if history:
                print("\nCalculation History:")
                for item in history:
                    print(item)
            else:
                print("No calculations yet.")
            continue

        if choice == '8':
            clear_screen()
            continue

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue

            if choice == '1':
                result = add(num1, num2)
                operation = f"{num1} + {num2} = {result}"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = f"{num1} - {num2} = {result}"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = f"{num1} * {num2} = {result}"
            elif choice == '4':
                result = divide(num1, num2)
                operation = f"{num1} / {num2} = {result}"
            elif choice == '5':
                result = modulus(num1, num2)
                operation = f"{num1} % {num2} = {result}"
            elif choice == '6':
                result = exponentiate(num1, num2)
                operation = f"{num1} ^ {num2} = {result}"

            print(operation)
            history.append(operation)
        else:
            print("Invalid choice! Please select a valid operation.")

# Run the calculator function
calculator()