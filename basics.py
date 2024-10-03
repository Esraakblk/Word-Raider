import re
with open("words.txt", "r") as file:
    lines = file.readlines()

with open("words.txt", "w") as file:
    for line in lines:
        cleaned_line = re.sub(r'\d+', '', line).strip()
        file.write(cleaned_line + '\n') 
       

file_path = "words.txt"
