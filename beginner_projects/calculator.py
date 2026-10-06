"""A beginner-friendly calculator CLI."""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def main():
    print("Simple Calculator")
    print("Operations: +, -, *, /")

    while True:
        try:
            first = float(input("Enter the first number: "))
            operator = input("Enter an operator (+, -, *, /): ").strip()
            second = float(input("Enter the second number: "))

            if operator == "+":
                result = add(first, second)
            elif operator == "-":
                result = subtract(first, second)
            elif operator == "*":
                result = multiply(first, second)
            elif operator == "/":
                result = divide(first, second)
            else:
                print("Invalid operator.")
                continue

            print(f"Result: {result}")
        except ValueError as error:
            print(f"Error: {error}")

        again = input("Do you want to calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
