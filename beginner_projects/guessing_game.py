"""A beginner number guessing game."""

import random


def main():
    secret_number = random.randint(1, 20)
    attempts = 5

    print("Welcome to the Number Guessing Game!")
    print("I picked a number between 1 and 20.")
    print(f"You have {attempts} attempts to guess it.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempt} attempts.")
            return

    print(f"Game over! The number was {secret_number}.")


if __name__ == "__main__":
    main()
