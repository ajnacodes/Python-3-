import random
# define words list
word_list = ["water", "pixel", "chocolate", "lucky", "lake", "banana", "plant", "painting"]
# get a random word from the list
chosen_word = random.choice(word_list)
print(chosen_word)

# create an empty list, then add a blank space to it for each letter in the chosen word
display = []
for letter in chosen_word:
    display += "_"
# print list with blank spaces
print(display)

# function that will keep the game running until no blank spaces are encountered
end_of_game = False
while not end_of_game:
    if "_" in display:
        guess = input("Guess a letter: ").lower()
        # loop through the chosen word and replace letters if the guess matches
        for space in range(len(chosen_word)):
            letter = chosen_word[space]
            if letter == guess:
                display[space] = letter
        print(display)
    else:
        print("You win!")
        end_of_game = True
