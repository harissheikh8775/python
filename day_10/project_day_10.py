from calculator_art import logo
import os

print(logo)


# ---------- Basic Operations ----------
def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mult(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero!"
    return num1 / num2


# Dictionary for operations
operations_dict = {"+": add, "-": sub, "*": mult, "/": divide}


# ---------- Calculator Logic ----------
def call_operation(num1, num2, operation):
    operation_func = operations_dict.get(operation)
    if operation_func:
        result = operation_func(num1, num2)
        print(f"{num1} {operation} {num2} = {result}")
        return result
    else:
        print("Invalid operation!")
        return None


# ---------- Main Program ----------
def calculator():
    should_continue = True
    num1 = float(input("What's the first number?: "))

    while should_continue:
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))

        result = call_operation(num1, num2, operation)

        next_step = input(
            f"Type 'y' to continue calculating with {result}, or 'n' to start a new calculation: "
        )

        if next_step == "y":
            num1 = result
        else:
            os.system("cls" if os.name == "nt" else "clear")
            print(logo)
            calculator()  # Restart calculator
            return


# ---------- Run Program ----------
calculator()
