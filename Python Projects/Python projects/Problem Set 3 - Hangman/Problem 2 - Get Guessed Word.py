#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 23:58:24 2020

@author: gabrieltutone
"""

secretWord = 'apple'
lettersGuessed = ['r', 'i', 'k', 'r', 'r', 'a']

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


print(getGuessedWord(secretWord, lettersGuessed))