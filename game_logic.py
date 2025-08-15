import random
from ascii_art import STAGES
from secret_words import WORDS

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage
    print(STAGES[mistakes])
    display_word = ""
    letter_count = 0

    # Display letters
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
            letter_count += 1
        else:
            display_word += "_ "
            mistakes += 1

    print(f"Word: {display_word}\n")
    if letter_count == len(secret_word):
        print("You won!")
        exit()



def play_game():
    mistakes = 0
    guessed_letters = []
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print(f"secret word: {secret_word}") # for testing


    while True:
        # Display game state
        display_game_state(mistakes, secret_word, guessed_letters)

        # For now, simply prompt the user once:
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        # add guess to list of guessed letters
        guessed_letters.append(guess)

        # count mistakes
        if guess not in secret_word:
            mistakes += 1

        # check if game is over
        if mistakes >= 3:
            print("Game over!")
            exit()