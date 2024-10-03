import random

game_title = "Word Raider"
word_list = [] 
with open("words.txt", "r") as file:
    for line in file:
        word = line.rsplit() # Remove trailing spaces and newline characters
        word_list.append(word) # Add the word to the word list

guess_the_word = random.choice(word_list)