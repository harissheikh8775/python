from black_jack_art import logo
import random

my_cards=[]
comps_cards=[]
first_card=rand

comp_pass=random.randrange(10)

def final_score(my_cards):
    sum=0
    for num in my_cards:
        sum+=num
    return sum


continue_game=True
while continue_game:
    move = input("Do you want to play a game of BlackJack? Type 'y' or 'n':  ")
    if move=='n':
        pass
    else:
        print(logo)
        next_card=input("Type 'y' to get another card, type 'n' to pass:  ")
        if next_card=="n":
            print(f"Your final hand : {my_cards}, final score: {final_score(my_cards=my_cards)}")
            print(f"Computer's final hand : {comps_cards}, final score {final_score(my_cards=comps_cards)}")

