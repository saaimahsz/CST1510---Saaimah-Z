# =================================
# PROJECT 1: ROCK, PAPER, SCISSORS
# =================================

import random

def get_computer_choice():
    """Return the computer's random choice."""
    number = random.randint(0, 2)

    if number == 0:
        return "rock"
    elif number == 1:
        return "paper"
    else:
        return "scissors"


def decide_winner(user_choice, computer_choice):
    """Decide the winner of the game."""
    if user_choice == computer_choice:
        return "draw"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "user"
    else:
        return "computer"


def play_rock_paper_scissors():
    """Play a game of Rock, Paper, Scissors."""
    user_choice = input(
        "Choose rock, paper or scissors: "
    ).strip().lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please choose rock, paper or scissors.")
        return

    computer_choice = get_computer_choice()
    print("Computer chose: ", computer_choice)
    winner = decide_winner(user_choice, computer_choice)

    if winner == "draw":
        print("It's a draw!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")



# =================================
# PROJECT 2: CALCULATOR
# =================================

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def calculator():
    """Perform calculations until user chooses to stop."""

    while True:
        try:
            n1 = float(input("Enter the first number: "))
            break
        except ValueError:
            print("Please enter a valid number!")
    
    keep_going = True


    while keep_going:
        operator = input("Choose an operator (+, -, *, /): ").strip()

        if operator not in ["+", "-", "*", "/"]:
            print("Invalid operator! Please choose +, -, *, or /.")
            continue

        while True:
            try:
                n2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Please enter a valid number!")

        if operator == "+":
            result = add(n1, n2)
        elif operator == "-":
            result = subtract(n1, n2)
        elif operator == "*":
            result = multiply(n1, n2)
        elif operator == "/":
            if n2 == 0:
                print("Error: Cannot divide by zero!")
                continue
            result = divide(n1, n2)
        else:
            print("Invalid operator!")
            continue

        print(n1, operator, n2, "=", result)

        answer = input(
            "Type 'y' to continue, 'n' to start over, or 'q' to quit: "
        ).strip().lower()

        if answer == "y":
            n1 = result
        elif answer == "q":
            keep_going = False
            print("Exiting calculator.")
        else:
            while True:
                try:
                    n1 = float(input("Enter a new first number: "))
                    break
                except ValueError:
                    print("Please enter a valid number!")



# =================================
# PROJECT 3: NUMBER GUESSING GAME
# =================================

def play_number_guessing_game():
    """Play a number guessing game!"""

    secret_number = random.randint(1, 100)
    guesses = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess_input = input(
            "Take a guess (1-100), or type 'q' to quit the game: "
        )

        if guess_input.lower() == "q":
            print("Leaving the Number guessing Game.")
            return

        try:
            guess = int(guess_input)
        except ValueError:
            print("Please enter a whole number, or 'q' to quit the game!")
            continue

        if guess < 1 or guess > 100:
            print("Enter a number between 1 and 100, or 'q' to quit the game!")
            continue
        
        guesses += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            print("Number of guesses: ", guesses)
            break



# =================================
# MAIN MENU
# =================================

if __name__ == "__main__":
    while True:
        print("\nChoose a project: ")
        print("1. Rock, Paper, Scissors")
        print("2. Calculator")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            play_rock_paper_scissors()
        elif choice == "2":
            calculator()
        elif choice == "3":
            play_number_guessing_game()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3, or 4.")
