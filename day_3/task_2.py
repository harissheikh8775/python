# Roller coster

print("Welcome to the roller coster.")

height = int(input("Please enter your height in cm? "))
age = int(input("Please enter you age? "))

if height > 120:
    print("You can ride.")
    if age > 18:
        print("Please pay $12.")
    elif age < 12:
        print("Pleaase pay $5")
    elif 18 < age > 12:
        print("Please pay $7")
else:
    print("You can't ride.")
