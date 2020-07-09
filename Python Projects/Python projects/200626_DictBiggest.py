#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 23:00:08 2020

@author: gabrieltutone
"""


animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati'], 'd': ['donkey', 'dog', 'dingo']}
#animals = {}

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    longest = 0
    longestKey = ''
    temp = 0
    for i in aDict:
        for e in aDict[i]:        #iterate through each item
            temp +=1
        if temp >= longest:         #only keep longest list
            longest = temp
            longestKey = i
            temp = 0
        else:
            temp = 0
    if longest == 0:
        return 'None'
    else:
        return longestKey

print(biggest(animals))