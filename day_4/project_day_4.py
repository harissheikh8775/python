import random

rock = """
   _______
---'   ____)
      (_____ )
      (_____ )
      (____ )
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

choice_list = [rock, paper, scissors]

# Take user input
my_choice_index = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
)

# Validate input
if my_choice_index < 0 or my_choice_index > 2:
    print("Invalid choice! You must choose 0, 1, or 2.")
else:
    my_move = choice_list[my_choice_index]

    # Computer's random choice
    comp_choice_index = random.randint(0, 2)
    comp_move = choice_list[comp_choice_index]

    # Show both choices
    print("You chose:")
    print(my_move)
    print("Computer chose:")
    print(comp_move)

    # Determine winner
    if my_choice_index == comp_choice_index:
        print("It's a Draw!!")
    elif (
        (my_choice_index == 0 and comp_choice_index == 2)
        or (my_choice_index == 1 and comp_choice_index == 0)
        or (my_choice_index == 2 and comp_choice_index == 1)
    ):
        print("You won the game!! 🎉")
    else:
        print("Computer won the game!! 💻")
