import random

from ascii_art import STAGES

WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    print(STAGES[mistakes])

    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print()


def play_game():
    while True:
        secret_word = get_random_word()
        guessed_letters = []
        mistakes = 0
        max_mistakes = len(STAGES) - 1

        print("\nWelcome to Snowman Meltdown!")

        while mistakes < max_mistakes:
            display_game_state(mistakes, secret_word, guessed_letters)

            guess = input("Guess a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.append(guess)

            if guess not in secret_word:
                mistakes += 1
                print("Wrong guess!")

            if all(letter in guessed_letters for letter in secret_word):
                display_game_state(mistakes, secret_word, guessed_letters)
                print("You saved the snowman!")
                break

        else:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("The snowman melted! The word was:", secret_word)

        play_again = input("\nPlay again? (y/n): ").lower()

        if play_again != "y":
            print("Thanks for playing!")
            break
