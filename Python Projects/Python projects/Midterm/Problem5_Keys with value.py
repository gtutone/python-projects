#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:06:02 2020

@author: gabrieltutone
"""
# Write a Python function that returns a list of keys in aDict with the value target. 
# The list of keys you return should be sorted in increasing order. 
# The keys and values in aDict are both integers. (If aDict does not contain the value target, 
# you should return an empty list.)

# This function takes in a dictionary and an integer and returns a list.


#dDict = {1:1, 2:2, 3:3, 4:4}

#bDict = {}

#cDict = {1:1, 2:2, 3:3, 4:100}

def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here
    
    # KeysinDict = aDict.keys()
    
    KeysinDict = []
    
    for i in aDict:
        if aDict[i] == target:
            KeysinDict.append(i)  
    
    # Sort KeysinDict in increasing order
    KeysinDict.sort()
    
    return KeysinDict


#print(keysWithValue(dDict, 4))
#print(keysWithValue(aDict, 5))
#print(keysWithValue(bDict, 1))
#print(keysWithValue(cDict, 4))

print(keysWithValue({9: 2, 10: 2, 3: 1, 2: 1, 6: 2}, 1))