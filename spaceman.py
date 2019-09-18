import random

secretWord = list()

def playAgain():
    ''' A function that checks whether play wants to play again.'''
    again = input("Would you like to play again? [y/n]")

    if again in ['Y', 'y', 'ye', 'yeah', 'ok']:
        playAgain = True
    else:
        playAgain = False
        
        

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('dictionary.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secretWord = random.choice(words_list)
    return secretWord

def is_word_guessed(secretWord, lettersGuessed):
    
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
        return True
    pass


def get_guessed_word(secretWord, lettersGuessed):

    alreadyGuessed = []

    for letter in secretWord:
        if letter in lettersGuessed:
            alreadyGuessed.append(letter)
        else:
            alreadyGuessed.append(" _ ")
    return alreadyGuessed
            
    
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    
    pass

def is_guess_in_word(guess, secretWord):

    
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''

    guess = input("Enter a letter: ")

    if guess in secretWord:
        print("the letter you guessed is in the word.")
        print("the new word is now:
    
    #TODO: check if the letter guess is in the secret word

    pass




def spaceman(secretWord):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    wordBank = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    tries = 26

    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secretWord = load_word()
spaceman(secretWord)
