"""A simple password generator CLI for beginners."""

import random
import string


def generate_password(length, use_uppercase, use_lowercase, use_numbers, use_symbols):
    """Generate a random password from the selected character types."""
    characters = ""
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        raise ValueError("Choose at least one character type.")
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    password = "".join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("=== Password Generator ===")

    while True:
        try:
            length = int(input("How long should the password be? ").strip())
            use_uppercase = input("Include uppercase letters? (y/n): ").strip().lower() == "y"
            use_lowercase = input("Include lowercase letters? (y/n): ").strip().lower() == "y"
            use_numbers = input("Include numbers? (y/n): ").strip().lower() == "y"
            use_symbols = input("Include symbols? (y/n): ").strip().lower() == "y"

            password = generate_password(
                length,
                use_uppercase,
                use_lowercase,
                use_numbers,
                use_symbols,
            )
            print(f"Your password is: {password}")
        except ValueError as error:
            print(f"Error: {error}")

        again = input("Generate another password? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
