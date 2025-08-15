import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]

def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage
    print(STAGES[mistakes])
    display_word = ""

    # Display letters
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
            mistakes += 1

    print(f"Word: {display_word}\n")

    return mistakes


def play_game():
    mistakes = 0
    secret_word = get_random_word()
    print("Welcome to Snowman Meltdown!")
    print(f"secret word: {secret_word}") # for testing
    guessed_letters = []

    while True:
        # check if user has won
        if len(secret_word) == len(guessed_letters):
            print("you won!")
            exit()

        # Display game state
        display_game_state(mistakes, secret_word, guessed_letters)


        # For now, simply prompt the user once:
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)
        guessed_letters.append(guess)
        if guess not in secret_word:
            mistakes += 1



if __name__ == "__main__":
    play_game()