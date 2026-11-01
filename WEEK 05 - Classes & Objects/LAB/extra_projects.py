# =================================
# PROJECT: BLACKJACK GAME
# =================================


import random


def deal_card():
    """Return a random card value."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


class Hand:
    """Store and calculate the score of a Blackjack hand."""

    def __init__(self):
        self.cards = []

    def add_card(self):
        """Deal one card and add it to this hand."""
        self.cards.append(deal_card())

    def score(self):
        """Calculate the hand's score, including ace rules."""
        total = sum(self.cards)
        aces = self.cards.count(11)
        
        # Count an ace as 1 instead of 11 if the score is too high.
        while total > 21 and aces > 0:
            total -= 10
            aces -= 1

        # A natural Blackjack is an ace and a 10-value card.
        if total == 21 and len(self.cards) == 2:
            return 0
        return total


def compare(user_score, computer_score):
    """Compare the final scores and return the result."""
    if user_score == computer_score:
        return "It's a draw!"
    elif user_score == 0:
        return "You win with a Blackjack!"
    elif computer_score == 0:
        return "Computer wins with a Blackjack!"
    elif user_score > 21:
        return "You went over 21. You lose!"
    elif computer_score > 21:
        return "Computer went over 21. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "Computer wins!"


def play_game():
    """Play one round of Blackjack."""
    user_hand = Hand()
    computer_hand = Hand()

    # Deal two cards to each hand.
    for _ in range(2):
        user_hand.add_card()
        computer_hand.add_card()

    print("\nYour cards:", user_hand.cards)
    print("Your score:", user_hand.score())

    # Show only the computer's first card at first.
    print("Computer's first card:", computer_hand.cards[0])

    # The player can draw more cards or stop.
    while user_hand.score() != 0 and user_hand.score() < 21:
        choice = input("Type 'y' to draw another card, or 'n' to pass: ").lower()

        if choice == "y":
            user_hand.add_card()
            print("Your cards:", user_hand.cards)
            print("Your score:", user_hand.score())

            if user_hand.score() > 21:
                break
        elif choice == "n":
            break
        else:
            print("Please type 'y' or 'n'.")

    # The computer draws until it reaches at least 17.
    if user_hand.score() <= 21:
        while computer_hand.score() != 0 and computer_hand.score() < 17:
            computer_hand.add_card()


    # Reveal both final hands.
    print("\n" + "-" * 35)
    print("         FINAL RESULTS")
    print("-" * 35)

    print("Your cards:", user_hand.cards)
    print("Your final score:", user_hand.score())

    print("Computer's cards:", computer_hand.cards)
    print("Computer's final score:", computer_hand.score())

    print("\nResult:", compare(user_hand.score(), computer_hand.score()))
    print("=" * 35)


# Test the Hand class
def test_hand_class():
    """Check that Hand scores work correctly."""

    test_hand = Hand()

    test_hand.cards = [10, 7]
    assert test_hand.score() == 17

    test_hand.cards = [11, 10]
    assert test_hand.score() == 0  # Natural Blackjack

    test_hand.cards = [11, 7, 9]
    assert test_hand.score() == 17  # Ace counts as 1

    test_hand.cards = [10, 5, 9]
    assert test_hand.score() == 24  # Bust

    print("All Hand class tests passed!")


if __name__ == "__main__":
    test_hand_class()

    while True:
        play_game()

        play_again = input(
            "\nWould you like to play again? Type 'y' or 'n': "
        ).lower().strip()

        if play_again != "y":
            print("Thank you for playing Blackjack!")
            break
