#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 13:18:23 2020

@author: gabrieltutone
"""

def f(i):
    return i + 2

def g(i):
    return i > 5

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    # Your code here
    
    if L == []:
        return -1
    
    else:
        newL = []
    
        for i in range(len(L)):
            if g(f(L[i])):
                newL.append(L[i])
        
        L[:] = newL
    
        #return largest element in new List
        if L == []:
            return -1
        else:
            return max(L)

L = [-10, -11, -12]
print(applyF_filterG(L, f, g))
print(L)