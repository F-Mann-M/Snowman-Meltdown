import random, os, platform, sys
from ascii_art import STAGES
from secret_words import WORDS

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """
    Takes in mistakes, secret word and a list of guessed letters
    Shows stage of Ascii art snowman
    compare guessed letters with secret word
    display correct letters
    """
    # Display the snowman stage
    print(STAGES[mistakes])
    display_word = ""
    # check if letter in secret word and display letter
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
            mistakes += 1
    print(f"Word: {display_word}\n")


def validate_input():
    """prompts user to enter a guess. checks if input is just one letter and returns user input"""
    while True:
        user_input = input("Guess a letter: ").lower()
        if len(user_input) == 1 and user_input.isalpha():
            print("You guessed:", user_input)
            return user_input
        else:
            print("Invalid input! Please enter a single letter.")


def clear_console():
    """clears console (only works in the (real) terminal)"""
    # Check system and clear the Screen
    if platform.system == "Windows":
        os.system("cls")
    else:
        os.environ.setdefault("TERM", "xterm")
        os.system("clear")



def check_final_conditions(guessed_letters, secret_word, mistakes):
    """checks whether the guessed correct letters correspond to the number of letters in the secret word."""
    # check whether the player won or lost
    letter_count = 0
    for letter in secret_word:
        if letter in guessed_letters:
            letter_count += 1
    if letter_count == len(secret_word):
        print("You won!")
    elif mistakes >= 4:
        print("Game over!")
    else:
        return None

    # Ask user to replay
    while True:
        user_choice = input("Want to play again (y/n): ")
        if user_choice.lower() == "y":
            play_game()
        elif user_choice.lower() == "n":
            exit()
        else:
            print("Invalid input. Please enter y or n")


def play_game():
    """executes the game logic"""
    mistakes = 0
    guessed_letters = []
    secret_word = get_random_word()

    while True:
        # clear display
        clear_console()
        print("Welcome to Snowman Meltdown!")
        #print(f"secret word: {secret_word}")  # for testing

        # Display game state
        display_game_state(mistakes, secret_word, guessed_letters)

        # check if game is over
        check_final_conditions(guessed_letters, secret_word, mistakes)

        # get user input and validate input
        guess = validate_input()

        # add guess to list of guessed letters
        guessed_letters.append(guess)

        # count mistakes
        if guess not in secret_word:
            mistakes += 1

