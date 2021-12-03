import random
import string

HANGMAN_PICS = ['''
    +---+
            |
            |
            |
        ===''', '''
    +---+
    0      |
            |
            |
        ===''', '''
    +---+
    O     |
     |      |
            |
        ===''', '''
    +---+
    O     |
    /\     |
            |
        ===''', '''
    +---+
    O     |
    /|\    |
            |

        ===''', '''
    +---+
    O     |
    /|\    |
    /      |
        ===''', '''
    +---+
    O     |
    /|\    |
    / \    |
        ===''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar\
                    coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk\
                    lion lizard llama mole monkey moose mouse mule newt otter owl panda\
                    parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep\
                    skunk sloth snake spider stork swan tiger toad trout turkey turtle\
                    weasel whale wolf wombat zebra'.split() #turned strings into list items

def get_word(): # chose a random word
    chosen_word = random.choice(words)
    return chosen_word

def display_intro(secret_word,correct_guess,missed_guess):
    print("___________________________________________________________________________________________")
    print(HANGMAN_PICS[len(missed_guess)]) #displayed the hangman corresponding to missed guess
    print("missed letters: ", end = " ")

    for letter in missed_guess: #printed all the missed letters with spaces between them
        print(letter, end=" ")
        
    print()
    
    blanks= '-'*len(secret_word) #printed blank corresponding to length of secret word


    for i in range(len(secret_word)):
        if secret_word[i] in correct_guess:
            blanks = blanks[:i] +secret_word[i]+blanks[i+1:] #replaced blanks with correct guess

    for dashes in blanks: #printed all the blanks with spaces between them
        print(dashes, end=" ")
    print()
    
def get_guess(alreadyguessed): #ask the user to guess a letter
    
    while True:
        user_guess = input("Guess a letter ").lower()
        if user_guess in alreadyguessed: #checked that the user hasn't guess this letter before
            print("You have guessed this letter before")
        elif user_guess not in string.ascii_lowercase:
            print("Please type a letter")
        elif len(user_guess) != 1:
            print("Please type just one letter")
        else:
            return user_guess

def play_again():
    replay = input("Do you want to play again? ").lower()
    return replay.startswith("y")

#default variables
correct_guess = ''
missed_guess = ''
secret_word = get_word()
display_intro(secret_word,correct_guess,missed_guess)
game_is_done = False


while True: #start the game 
    guess = get_guess(correct_guess+missed_guess)

    if guess in secret_word:
        correct_guess += guess
        display_intro(secret_word,correct_guess,missed_guess)

        # check if player has won
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_guess:
                found_all_letters = False

        if found_all_letters:
            print(f"Yes the secret word was {secret_word}, you have won")
            game_is_done = True
    else:
        missed_guess += guess
        display_intro(secret_word,correct_guess,missed_guess)
        if len(missed_guess) == len(HANGMAN_PICS)-1: #check if the user is out of guess
            print(f"After {len(missed_guess)} missed guess and {len(correct_guess)} correct guess, "
                  f"you have run out of guesses. The correct word was {secret_word}")
            game_is_done = True
    #run the code again if user wants to play again
    if game_is_done:
        if play_again():
            correct_guess = ''
            missed_guess = ''
            secret_word = get_word()
            game_is_done = False
            display_intro(secret_word,correct_guess,missed_guess)
        else:
            break


