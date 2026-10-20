# =================================
# PROJECT 1: PYTHON PIZZA
# =================================

size = input("What size pizza? (S, M, L): ")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 0
    print("Invalid pizza size")

pepperoni = input("Do you want pepperoni? (Y/N): ")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or size == "L":
        bill += 3

cheese = input("Do you want extra cheese? (Y/N): ")

if cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")



# =================================
# PROJECT 2: TREASURE ISLAND
# =================================

print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")

choice1 = input("You've reached a cross road. Left or right? ").lower()

if choice1 == "left":
    choice2 = input("You've reached a lake. Swim or wait? ").lower()

    if choice2 == "wait":
        choice3 = input("Three doors appear: red, blue, and yellow. Which one do you choose? ").lower()

        if choice3 == "yellow":
            print("You found the treasure! You win!")
        elif choice3 == "red":
            print("You were burned by fire. Game over!")
        elif choice3 == "blue":
            print("You were eaten by beasts. Game over!")
        else:
            print("That door doesn't exist. Game over!")
    else:
        print("You were attacked by a trout. Game over!")
else:
    print("You fell into a hole. Game over!")



# =================================
# PROJECT 3: HIGHER OR LOWER GAME
# =================================

# Compare two follower counts and keep playing until quit.

account_a = 150
account_b = 250

while True:
    print(f"Account A has, {account_a}, followers.")
    print(f"Account B has, {account_b}, followers.")

    guess = input("Which account has more followers? Type 'A' or 'B' (or quit): ").lower()

    if guess == "quit":
        print("Thanks for playing!")
        break
    elif guess == "a" and account_a > account_b:
        print("You guessed correctly!")
    elif guess == "b" and account_b > account_a:
        print("You guessed correctly!")
    else:
        print("Sorry, that's incorrect!")



# =================================
# PROJECT 4: NUMBER GUESSING GAME
# =================================

secret_number = 7
guesses = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")

while True:
    guess = int(input("Take a guess: "))
    guesses += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
        print("Number of guesses:", guesses)
        break
    