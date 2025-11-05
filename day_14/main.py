from art import logo, vs
from game_data import data
import random
import os


def clear_screen():
    # Works on both Windows and macOS/Linux
    os.system("cls" if os.name == "nt" else "clear")


def play_game():
    print(logo)
    score = 0
    game_should_continue = True

    # Start with a random A
    person_a = random.choice(data)

    while game_should_continue:
        # Pick a random B that is not the same as A
        person_b = random.choice(data)
        while person_b == person_a:
            person_b = random.choice(data)

        # Display info for A and B
        print(
            f"Compare A: {person_a['name']}, a {person_a['description']} from {person_a['country']}."
        )
        print(vs)
        print(
            f"Against B: {person_b['name']}, a {person_b['description']} from {person_b['country']}."
        )

        # Ask user for choice
        choice = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

        # Get follower counts
        a_followers = person_a["follower_count"]
        b_followers = person_b["follower_count"]

        # Check answer
        is_correct = (choice == "A" and a_followers > b_followers) or (
            choice == "B" and b_followers > a_followers
        )

        clear_screen()
        print(logo)

        if is_correct:
            score += 1
            print(f"✅ You're right! Current score: {score}.\n")
            # Winner becomes next A
            person_a = person_b
        else:
            print(f"❌ Sorry, that's wrong. Final score: {score}\n")
            game_should_continue = False


# Main loop with replay feature
while True:
    play_game()
    replay = input("Do you want to play again? Type 'y' or 'n': ").strip().lower()
    if replay != "y":
        print("Thanks for playing! 👋")
        break
    clear_screen()
