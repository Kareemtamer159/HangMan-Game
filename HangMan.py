import random
import hangmanParts
from hangmanWords import Words,hints

print(hangmanParts.logo)

print("Welcome To HangMan Game 🎮")

secret_word = random.choice(Words)  ## Randomly select a word from the list of words

## create blanks of the word 
place_holder = ""
for position in range(len(secret_word)):
    place_holder += "_ "

print("Guess the word:", place_holder)##the player guess the word

lives = 6 # the player has 6 lives
 
game_end = False #this is the condition that make the loop run the
wrong_letters_guessed = [] # this is the list of all letters guessed by the player 
correct_guess = [] # the player has not guessed any letter yet
index = Words.index(secret_word)##hint when there is 1 attempt

while not game_end:
    guess = input("Enter a letter: ").lower()
    
    if (guess in correct_guess) or (guess in wrong_letters_guessed):  ## Check if the letter is already guessed
        print(f"You've already guessed that letter '{guess}', Try Again!!")
        continue
    final_word = ""

    for letter in secret_word: 
        ## Check if the letter is guessed correctly
        if letter == guess:
            final_word += letter ## if the letter is guessed correctly
            correct_guess.append(guess) ##added to correct guess list
        elif letter in correct_guess: ## if the letter is already guessed correctly
            final_word += letter ##to prevent remove the letter from the final word
        else:
            final_word += "_ "
    
    print(final_word)        

## Check if the user has guessed the word or lost all lives
    if "_" not in final_word:
        print("😁🥳🥳Congratulations! You've guessed the word:", secret_word)
        game_end = True
    else:
        if guess not in secret_word:
            lives -= 1
            wrong_letters_guessed.append(guess)
            print(f"❌ Wrong guess! Lives left: {lives}/6 ")
            print(hangmanParts.HANGMANPICS[lives])
            if lives == 1:## give hint when there is 1 attempt left
                print("IT's A Time For Hint 💡💡 : ")
                print("💡 Hint:", hints[index])
            if lives == 0:
                print("😔😔Game Over! The word was:", secret_word)
                game_end = True

print("\nThanks for playing! 👋")

