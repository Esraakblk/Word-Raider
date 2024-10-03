import random

game_title = "Word Raider"
word_list = [] 
with open("words.txt", "r") as file:
    for line in file:
        word = line.rsplit() # Remove trailing spaces and newline characters
        word_list.append(word) # Add the word to the word list

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

