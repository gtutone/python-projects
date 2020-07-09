#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 21:25:00 2020

@author: gabrieltutone
"""

from ps4a import *

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # Create copy of the hand
    handCopy = hand.copy()
    
    # For each letter in the word, subtract 1 from hand
    for letter in word:
        handCopy[letter] = handCopy.get(letter, 1) - 1
    
    return handCopy

handTest = {'a':1, 'p':2, 'l':3, 'e':4}
wordTest = 'apple'
print(updateHand(handTest, wordTest))
print(handTest)
displayHand(handTest)