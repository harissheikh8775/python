# treasure island project

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