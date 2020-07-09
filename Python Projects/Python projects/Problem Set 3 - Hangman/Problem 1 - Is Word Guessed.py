#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 23:04:45 2020

@author: gabrieltutone
"""

secretWord = 'apple'
lettersGuessed = ['a', 'i', 'l', 'p', 'r', 'e']

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

print(isWordGuessed(secretWord, lettersGuessed))