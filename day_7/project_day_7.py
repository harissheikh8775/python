# -----------------------------#
#        HANGMAN PROJECT       #
# -----------------------------#

import random
import hangman_words  # module containing the word list
import hangman_art  # module containing logo and stages (ASCII art)

# Print the Hangman game logo
print(hangman_art.logo)

# Randomly choose a word from the imported word list
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)  # (You can comment this out later for real gameplay)

# Total lives a player has
lives = 6

# Create an initial placeholder (e.g., "apple" -> "_____")
placeholder = "_" * len(chosen_word)
print(placeholder)

game_over = False
correct_letters = []  # To store correctly guessed letters

# -----------------------------#
#        MAIN GAME LOOP        #
# -----------------------------#
while not game_over:
    print(f"\n********** {lives}/6 LIVES LEFT **********")

    guess = input("Guess a letter: ").lower()

    # Check if the letter was already guessed
    if guess in correct_letters:
        print(f"You've already guessed '{guess}'. Try another letter.")
        continue

    display = ""

    # Update the display for each letter in the chosen word
    for letter in chosen_word:
        if letter == guess:
            # If guessed letter matches, reveal it
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            # Keep previously guessed correct letters visible
            display += letter
        else:
            # Hide letters not yet guessed
            display += "_"

    # Show the current word progress
    print("Word to guess: " + display)

    # If the guessed letter is not in the chosen word
    if guess not in chosen_word:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1
        # Print the hangman stage according to remaining lives
        print(hangman_art.stages[lives])
        if lives == 0:
            game_over = True
            print("\n******************** YOU LOSE ********************")

    # Check if there are no more underscores (word completely guessed)
    if "_" not in display:
        game_over = True
        print("\n******************** YOU WIN ********************")
