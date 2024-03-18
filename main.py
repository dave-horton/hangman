import random
from hangman_words import word_list
from hangman_art import logo, stages

print(logo)

play = True
while play:
    #Randomly choose a word from the word_list and assign it to a variable. Set lives to 6 and end_of_game to False
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    end_of_game = False
    lives = 6

    #Cheat for test purposes.
    #print(f"chosen word is {chosen_word}")

    #Create a list of blanks for each letter in chosen_word. Print list.
    display = []
    for i in range(word_length):
        display += "_"
    print(f"{' '.join(display)}")

    #While game is still running. (No winner or loser yet)
    while not end_of_game:
        #Ask the user to guess a letter and assign their answer to a variable. Make sure it's lowercase.
        guess = input("Guess a letter: ").lower()
        if guess in display:
            print(f"You've already guessed {guess}")

        #Check if the guessed letter is in chosen_word and change the display list appropriately.
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        #If guess is incorrect, lose a life and check for end of game. 
        if guess not in chosen_word:
            lives -= 1
            print(f"{guess} is not correct. You are one step closer to being hanged!")
            if lives == 0:
                end_of_game = True
                print('Oh no! You have been hanged!')

        #Show the current word and guesses.
        print(f"{' '.join(display)}")

        #Check for win condition
        if "_" not in display:
            end_of_game = True
            print('You escaped the gallows! Congratulations!')
        
        #Print gallows art
        print(stages[lives])
    
    #Ask if they want to play again.
    play_again = input("Would you like to play again? Type yes to continue.").lower()
    if play_again == "yes":
        continue
    
    else:
        print(f"Thanks for playing!")
        play = False