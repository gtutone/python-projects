# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # Break down unique letters in the word
    if lettersGuessed == []:
        return False
    uniqueWord  = []
    guessed = []
    for i in secretWord:
        if i not in uniqueWord:
            uniqueWord.append(i)
    # Check if word is in guessed letters
    for e in uniqueWord:
        if e in lettersGuessed:
            guessed.append(e)
    if len(guessed) == len(uniqueWord):
        return True
    # If letter in word is not in guessed letters, return False
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    GuessedWord = ''
    # Iterate over secret Word
    for i in secretWord:
    # If letter is in lettersGuessed, add letter to GuessedWord string
        if i in lettersGuessed:
            GuessedWord = GuessedWord + i
    # If letter is NOT in lettersGuessed, add underscore to GuessedWord string
        else:
            GuessedWord = GuessedWord + ' _ '
    # Return GuessedWord string
    return GuessedWord

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    avaLetters = string.ascii_lowercase
    for i in lettersGuessed:
        if i in avaLetters:
            avaLetters = avaLetters.replace(i, '')
    return avaLetters

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    playerGuess = ''
    guesses = 8
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is', str(len(secretWord)), 'letters long.')

    while guesses > 0 and isWordGuessed(secretWord, lettersGuessed) == False:
        print('-------------')
        print('You have', guesses, 'guesses left.')
        print('Available letters:', str(getAvailableLetters(lettersGuessed)))
        playerGuess = input('Please guess a letter: ')
        playerGuess = playerGuess.lower()
        
        if playerGuess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))     
        
        elif playerGuess in secretWord:
            lettersGuessed.append(playerGuess)
            print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
        
        else:
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            guesses -= 1
            lettersGuessed.append(playerGuess)    
    
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print('------------')
        print('Congratulations, you won!')
    
    else:
        print('------------')
        print('Sorry, you ran out of guesses. The word was', secretWord)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

#secretWord = chooseWord(wordlist).lower()
secretWord = 'sea'
hangman(secretWord)
