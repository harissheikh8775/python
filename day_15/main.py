MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    },
}

resources = {"water": 300, "milk": 200, "coffee": 100}
money = 0


def has_resources(drink):
    """Check if machine has enough ingredients"""
    for item, required in MENU[drink]["ingredients"].items():
        if resources[item] < required:
            print(f"Sorry, not enough {item}.")
            return False
    return True


def process_coins():
    """Return total from inserted coins."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return quarters + dimes + nickels + pennies


def make_coffee(drink):
    """Deduct ingredients from machine."""
    for item, amount in MENU[drink]["ingredients"].items():
        resources[item] -= amount


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")

is_on=True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=="off":
        is_on=False
    if choice == "report":
        report()
        continue

    if choice not in MENU:
        print("Shut down the machine.")
        continue

    # Resource check
    if not has_resources(choice):
        continue

    # Payment
    payment = process_coins()
    cost = MENU[choice]["cost"]

    if payment < cost:
        print("Sorry, that's not enough money. Money refunded.")
        continue

    change = payment - cost
    if change > 0:
        print(f"Here is ${change:.2f} in change.")

    money += cost
    make_coffee(choice)
    print(f"Here is your {choice}. Enjoy!")
