import random
from hangman_words import word_list
# add stages
from hangman_art import stages
# define game status
end_of_game = False
# define words list
word_list = ["water", "pixel", "chocolate", "lucky", "lake", "banana", "plant", "painting"]
# get a random word from the list
chosen_word = random.choice(word_list)

# set stage of life
lives = 6
stages[lives]

from hangman_art import logo
print(logo)

# print(f"The word is:{chosen_word}.")


# create an empty list, then add a blank space to it for each letter in the chosen word
display = []
for letter in chosen_word:
    display += "_"



# function that will keep the game running until no blank spaces are encountered

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed the letter {guess}.")
        
    if "_" in display:
        
        # loop through the chosen word and replace letters if the guess matches
        for space in range(len(chosen_word)):
            letter = chosen_word[space]
            if guess == letter:
                display[space] = guess
        # join all the elements in the list and turn it into a string
        print(f"{' '.join(display)}")
        
    
        
    # set end of game depending on the lives left
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"You guessed {guess}, that's not in the word. Lives left: {lives}.")
    elif guess in chosen_word:
        print(stages[lives])
        
    if lives == 0:
        end_of_game = True
        print("You lose. No more lives.")
        print(f"The word was: {chosen_word}.")

    if "_" not in display:
        print("You win!")
        end_of_game = True
             
