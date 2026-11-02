# =================================
# PROJECT 1: HANGMAN
# =================================


import random


def play_hangman():
    """Play a game of Hangman by guessing a hidden word."""

    word_list = ["python", "network", "security", "hacker", "cipher"]
    chosen_word = random.choice(word_list)

    guessed_letters = []
    lives = 6

    print("\n=== HANGMAN ===")
    print("Guess the hidden word, one letter at a time!")

    while lives > 0:
        display = ""

        for letter in chosen_word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display.strip())
        print("Lives remaining:", lives)

        if "_" not in display:
            print("Congratulations! You guessed the word!")
            break

        guess = input("Guess a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter only.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in chosen_word:
            print("Correct guess!")
        else:
            lives -= 1
            print("Wrong guess! You lost a life.")

    if lives == 0:
        print("Game over! The word was:", chosen_word)



# =================================
# PROJECT 2: CAESAR CIPHER
# =================================

def encrypt(original_text, shift_amount):
    """Encrypt text by shifting each letter forwards."""
    encrypted_text = ""

    for letter in original_text:
        if letter.isalpha():
            alphabet = "abcdefghijklmnopqrstuvwxyz"
            is_uppercase = letter.isupper()
            letter = letter.lower()

            index = alphabet.index(letter)
            new_index = (index + shift_amount) % 26
            new_letter = alphabet[new_index]

            if is_uppercase:
                new_letter = new_letter.upper()

            encrypted_text += new_letter
        else:
            encrypted_text += letter

    return encrypted_text


def decrypt(original_text, shift_amount):
    """Decrypt text by shifting each letter backwards."""
    return encrypt(original_text, -shift_amount)


def caesar_cipher():
    """Let the user encrypt or decrypt a message."""
    print("\n=== CAESAR CIPHER ===")
    direction = input("Type 'encrypt' or 'decrypt': ").lower().strip()

    if direction not in ["encrypt", "decrypt"]:
        print("Invalid choice. Please type encrypt or decrypt.")
        return

    message = input("Enter your message: ")

    try:
        shift = int(input("Enter the shift amount: "))
    except ValueError:
        print("Please enter a whole number for the shift.")
        return

    if direction == "encrypt":
        result = encrypt(message, shift)
    else:
        result = decrypt(message, shift)

    print("Result:", result)



# =================================
# MAIN MENU
# =================================

def main():
    """Display the menu for the extra projects."""
    while True:
        print("\n=== WEEK 7 EXTRA PROJECTS ===")
        print("1. Hangman")
        print("2. Caesar Cipher")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            play_hangman()
        elif choice == "2":
            caesar_cipher()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
