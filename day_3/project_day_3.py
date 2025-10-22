# treasure island project
print(
'''

*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at the cross road. Where do you want to go? ")
side=input('       Type "left" or "right" ')

if side=="right":
    print("Fall into a hole.\nGame over.")
elif side=="left":
    swim=input("Do you want to swim? Y or N: ")
    wait=input("Do you want to wait? Y or N: ")
    if swim=="Y":
        print("Attacked by a trout.\nGame over.")
    elif wait=="Y":
        door=input("Which door do you want to go? red, blue, or yellow or anything else: ")
        if door=="red":
            print("Burned by fire.\nGame over.")
        elif door=="blue":
            print("Eaten by beasts.\nGame over.")
        elif door=="yellow":
            print("Congrats! You won the Game!!!.")
        else:
            print("Game over!!")
    else:
        print("Game over!!")
