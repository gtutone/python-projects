#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 12:14:46 2020

@author: gabrieltutone
"""
# Test middle character, see if it matches selected character
# If no match, is it smaller or bigger?
# BASE CASE
# What happens when the string is empty?
# What happens when the string is of length 1?
# What happens when the test character equals the middle character?
# RECURSIVE CASE
# What happens when the test character is smaller than the middle character?
# What happens when it is larger?

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == "":
        return False
    middle = aStr[int((0 + len(aStr))/2)]
    if char == middle:
        return True
    elif middle == "":
        return False
    elif len(aStr) == 1:
        return False
    elif char < middle:
        return isIn(char, aStr[0:int(len(aStr)/2)])
    elif char > middle:
        return isIn(char, aStr[int(len(aStr)/2):])


isIn("z", "")