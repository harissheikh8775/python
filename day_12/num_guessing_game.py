from num_art import logo
import random
import os


def clear_screen():
    """Clears the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def set_difficulty():
    """Returns number of attempts based on chosen difficulty."""
    while True:
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == "easy":
            return 10
        elif difficulty == "hard":
            return 5
        else:
            print("Invalid choice! Please type 'easy' or 'hard'.")


def check_guess(guess, target, lives):
    """Checks the user's guess and returns remaining lives."""
    if guess > target:
        print("Too high.")
        return lives - 1
    elif guess < target:
        print("Too low.")
        return lives - 1
    else:
        print(f"🎉 You got it! The answer was {target}.")
        return -1  # signal correct guess


def play_game():
    """Main function to play the Number Guessing Game."""
    clear_screen()
    print(logo)
    print("Welcome to the Number Guessing Game!!!")
    print("I'm thinking of a number between 1 and 100.")

    target_number = random.randint(1, 100)
    lives = set_difficulty()

    while lives > 0:
        print(f"\nYou have {lives} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        result = check_guess(guess, target_number, lives)

        if result == -1:
            break
        else:
            lives = result

        if lives == 0:
            print(
                f"💀 You've run out of guesses. The number was {target_number}. You lose."
            )


def main():
    """Driver function to start and replay the game."""
    while True:
        play_game()
        replay = input("\nDo you want to play again? Type 'y' or 'n': ").lower()
        if replay != "y":
            print("👋 Thanks for playing! Goodbye!")
            break
        clear_screen()


if __name__ == "__main__":
    main()


# **********************EASY LEVEL****************************
"""from num_art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!!!")
print("I'm thinking of a number between 1 and 100.")

# Generate a random number
random_number = random.randint(1, 100)

# Choose difficulty
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

# Set lives based on difficulty
lives = 10 if difficulty == "easy" else 5
print(f"You have {lives} attempts remaining to guess the number.")

# Game loop
while lives > 0:
    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess == random_number:
        print(f"🎉 You got it! The answer was {random_number}.")
        break
    elif guess > random_number:
        print("Too high.")
    else:
        print("Too low.")

    lives -= 1

    if lives > 0:
        print(f"Guess again. You have {lives} attempts remaining.")
    else:
        print(
            f"💀 You've run out of guesses. The number was {random_number}. You lose."
        )
"""
