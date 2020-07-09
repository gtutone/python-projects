#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:31:10 2020

@author: gabrieltutone
"""

from ps4a import *

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # Copy hand and subtract 1 for each letter value
    handCopy = hand.copy()
    for letter in word:
        handCopy[letter] = handCopy.get(letter, 0) - 1
    
    # If letter < 0, then word must be invalid
    for letter in handCopy:
        if handCopy[letter] < 0:
            return False
    
    # Check if word is in wordlist  
    if word in wordList:
        return True
    else:
        return False


hand = {'a':1, 'p':2, 'l':3, 'e':4}
word = 'zebra'
wordList = loadWords()
print(isValidWord(word, hand, wordList))