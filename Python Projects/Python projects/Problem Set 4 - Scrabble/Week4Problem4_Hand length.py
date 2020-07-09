#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 22:54:05 2020

@author: gabrieltutone
"""


def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    handLen = 0
    
    for letter in hand:
        handLen += hand.get(letter, 0)
    
    return handLen


hand = {'a':1, 'p':2, 'l':3, 'e':3}
print(calculateHandlen(hand))