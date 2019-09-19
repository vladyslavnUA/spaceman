import random

secretWord = list()

def loadWord():
    f = open('dictionary.txt', 'r')
    wordsList = f.readlines()
    f.close()
    
    wordsList = wordsList[0].split(' ')
    secretWord = random.choice(wordsList)
    return secretWord

def playAgain():
    again = input("Would you like to play again? [y/n]")

    if again in ['Y', 'y', 'ye', 'yeah', 'ok']:
        return True #playAgain = True
    else:
        return False #playAgain = False

def isWordGuessed(secretWord, lettersGuessed): 
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
    return True
    #pass

def getGuessedWord(secretWord, lettersGuessed):

    alreadyGuessed = []
    
    for letter in secretWord:
        if letter in lettersGuessed:
            alreadyGuessed.append(letter)
        else:
            alreadyGuessed.append(" _ ")
    return alreadyGuessed
    #pass

def isGuessInWord(guess, secretWord):          
    for letter in secretWord:
        if (guess == letter): #if guess equals letter value of input
            return True #return true
    return False #return false

def letterInWord(guess, secretWord):
    for letter in secretWord:
        if letter == guess:
            return True
    return False

def playAgain():
    again = input("Would you like to play again? [y/n]")

    if again in ['Y', 'y', 'ye', 'yeah', 'ok']:
        return True #playAgain = True
    else:
        return False #playAgain = False
        

def spaceman(secretWord):
    wordBankUniversal = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    attempts = 7 #industry standard
    lettersGuessed  = list()
    print(secretWord)

    print("-----------  W E L C O M E   T O   S P A C E M A N  -----------")
    print(" ")
    print("in spaceman, you will enter a letter to guess the secret word")
    print("you have only 7 tries, use 'em wisely.")

    while True:
    #(isWordGuessed(secretWord, lettersGuessed) == False and attempts > 0):
        print("the word contains " + str(len(secretWord)) + " letters.") #this should output the string stating the length amount of the word.
        guess = input("enter a single letter: ")   #ONE LETTER ONNLLLYYYY!!!!
        
        if len(guess) != 1:   #checks if player knows what one letter means
            print("invalid entry. try again [demon]")
            
        if guess not in wordBankUniversal:
            print("you have already used this letter")
            print(' '.join(getGuessedWord(secretWord, lettersGuessed)))
            continue #the program to check whether the guess is correct

        if guess in wordBankUniversal:
            wordBankUniversal.remove(guess)

        if letterInWord(guess, secretWord) == True:
            lettersGuessed.append(guess) #if the guess is correct, add guess to secretWord
            print("good job. the letter seems to be in the secret word.\nword progress:") #new line, print code below
            print(''.join(getGuessedWord(secretWord, lettersGuessed)))

            if isWordGuessed(secretWord, lettersGuessed) == True:
                print("yay, you win. [fireworks]")
                print(f"the secret word is {secretWord}!")
                break

            print("leftover letters: " + ''.join(str(a) for a in wordBankUniversal)) #get leftover letters from universal word bank.

        else:
            if attempts == 0:
                print("game over. [crying face]")
                playAgain()
            else:
                attempts = attempts - 1
                print("sorry, try again.")
                print(f"\nyou have {attempts + 1} incorrect guesses left.\nsecret word: " + ''.join(getGuessedWord(secretWord, lettersGuessed)))
                print("letters still in word bank: " + ''.join(str(a) for a in wordBankUniversal) + " ")  

#These function calls that will start the game
running = True
while running:
    secretWord = loadWord()
    spaceman(loadWord)
    running = playAgain()

#with starter code:    
#secretWord = loadWord()
#spaceman(secretWord)
