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

    #Check each Letter in the guess against the word's letters
    index = 0
    for i in the_guess:
        if i == guess_the_word[index]:
            print(i, end=" ")
            if i in misplaced_guesses:
                misplaced_guesses.remove(i)
        elif i in guess_the_word:
            if i not in misplaced_guesses:
                misplaced_guesses.append(i)
            print("_", end=" ")
        else:
            if i not in incorrect_guesses:
                incorrect_guesses.append(i)
            print("_", end=" ")
        index += 1

    print("\n")
    print(f"Misplaced letters: {misplaced_guesses}")
    print(f"Incorrect letters: {incorrect_guesses}")
    turns_taken += 1

    #Check if the player has won
    if the_guess == guess_the_word:
        print(f"Congratulations! You made a valid guess: {guess_the_word}")
        break

    #If the user reaches the maximum turns of rounds
    if turns_taken == max_turns:
        print(f"Sorry, you lost. You have {max_turns} rounds to guess the word.")
        print(f"The word was {guess_the_word}")
        break
    
    print(f"You have {max_turns - turns_taken} turns left." )
