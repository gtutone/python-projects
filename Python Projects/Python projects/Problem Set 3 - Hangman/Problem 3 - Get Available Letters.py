#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 00:40:20 2020

@author: gabrieltutone
"""

lettersGuessed = ['a', 'i', 'k', 'p', 'r', 's']


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # string.ascii_lowercase
    import string
    avaLetters = string.ascii_lowercase
    
    for i in lettersGuessed:
        if i in avaLetters:
            avaLetters = avaLetters.replace(i, '')
    
    return avaLetters

print(getAvailableLetters(lettersGuessed))