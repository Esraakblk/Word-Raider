import random

game_title = "Word Raider"
word_list = [] 
with open("words.txt", "r") as file:
    for line in file:
        word = line.rstrip() # Remove trailing spaces and newline characters
        word_list.append(word.lower()) # Add the word to the word list

guess_the_word = random.choice(word_list)

# Variables to keep track of game information
misplaced_guesses = []
incorrect_guesses = []
max_turns = 5
turns_taken = 0


#Player redirects
print(f"Welcome to {game_title}")
print(f"The word you have to guess consists of {len(guess_the_word)} letters.")
print(f"You have {max_turns} rounds to guess the word")

while turns_taken<max_turns:
    the_guess= input("What is your guess?").lower() #Asking the user to make guesses

    # Check the length of the guess and if it consists of only alphabetic characters.
    if len(the_guess) != len(guess_the_word):
        print(f"Error! The guessed word must be {len(guess_the_word)} characters long.")
        continue
    if not the_guess.isalpha():
        print("Error! The guess must contain only letters.")
        continue
    if the_guess == guess_the_word:
        print(f"Congratulations! You made a valid guess: {guess_the_word}")
        break
    else:
        print("Sorry, you made an invalid guess, try again!")
        continue
