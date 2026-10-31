# =================================
# PROJECT 1: BANKER ROULETTE
# =================================

import random

friends = ["Noah", "Melek", "Samiuel", "Sabina"]

print(random.choice(friends))

random_index = random.randint(0, len(friends) -1)
print(friends[random_index])



# =================================
# PROJECT 2: PASSWORD GENERATOR
# =================================

import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
symbols = list("!@#$%^&*()_+-=")
numbers = list("0123456789")

letter_count = int(input("How many letters would you like? "))
symbol_count = int(input("How many symbols would you like? "))
number_count = int(input("How many numbers would you like? "))

password = ""

for _ in range(letter_count):
    password += random.choice(letters)

for _ in range(symbol_count):
    password += random.choice(symbols)

for _ in range(number_count):
    password += random.choice(numbers)

print("Easy password: ", password)

password_characters = []

for _ in range(letter_count):
    password_characters.append(random.choice(letters))

for _ in range(symbol_count):
    password_characters.append(random.choice(symbols))

for _ in range(number_count):
    password_characters.append(random.choice(numbers))

random.shuffle(password_characters)

password = "".join(password_characters)

print("Hard password: ", password)



# =================================
# PROJECT 3: BLIND AUCTION
# =================================

bids = {}
another_bidder = "yes"

while another_bidder == "yes":
    name = input("What is your name? ")
    bid = float(input("What is your bid? £"))

    bids[name] = bid

    another_bidder = input("Is there another bidder? Type 'yes' or 'no':").lower()

highest_bid = 0
winner = ""

for name, bid in bids.items():
    if bid > highest_bid:
        highest_bid = bid
        winner = name

print(f"The winner is {winner} with a bid of £{highest_bid:.2f}")



# =================================
# PROJECT 4: COFFEE MACHINE
# =================================

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5
    },
    "cappucino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0
    }
}

def is_resource_sufficient(drink):
    ingredients = MENU[drink]["ingredients"]

    for item, amount in ingredients.items():
        if resources.get(item, 0) < amount:
            print(f"Sorry, there is not enough {items}!")
            return False

    return True

def process_payment(cost):
    payment = float(input(f"Your drink costs £{cost:.2f}. Please insert payment: £"))

    if payment < cost:
        print("Sorry, thats not enough money. Money refunded.")
        return False

    change = payment - cost

    if change > 0:
        print(f"Here is your change: £{change:.2f}")

    return True

def make_coffee(drink):
    ingredients = MENU[drink] ["ingredients"]

    for item, amount in ingredients.items():
        resources[item] -= amount

    print(f"Here is your {drink}. Enjoy!")

machine_on = True

while machine_on:
    choice = input("What would you like? (espresso/latte/cappucino): ").lower()

    if choice == "off":
        machine_on = False
    elif choice == "report":
        print("Current resources: ")
        for item, amount in resources.items():
            unit = "ml" if item in ("water", "milk") else "g"
            print(f"{item.title()}: {amount}{unit}")
    elif choice in MENU:
        drink = MENU[choice]

        if is_resource_sufficient(choice):
            if process_payment(drink["cost"]):
                make_coffee(choice)
    else:
        print("Invalid choice! Please choose espresso, latte, cappuccino, report or off.")
    