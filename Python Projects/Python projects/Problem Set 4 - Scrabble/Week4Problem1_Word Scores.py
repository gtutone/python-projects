#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 17:35:30 2020

@author: gabrieltutone
"""

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # if len(word) == n
    # Score = sum(word values) * len(word) + 50
    
    wordValue = 0
    
    if len(word) == n and len(word) != 0:
        for i in word:
            wordValue += SCRABBLE_LETTER_VALUES[i]
        return (wordValue * len(word)) + 50
    
    else:
        for i in word:
            wordValue += SCRABBLE_LETTER_VALUES[i]
        return wordValue * len(word)

print(getWordScore('apple', 5))

print(getWordScore('apple', 0))

print(getWordScore('apple', 100))

print(getWordScore('apple', 1))

print(getWordScore('apple', 0))

print(getWordScore('a', 5))

print(getWordScore('a', 1))

print(getWordScore('a', 0))

print(getWordScore('', 0))

print(getWordScore('', 5))







