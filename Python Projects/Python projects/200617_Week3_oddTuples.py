#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 20:35:42 2020

@author: gabrieltutone
"""

aTup = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    newTup = ()
    counter = 0
    for i in range(len(aTup)):
        if i % 2 == 0:
            newTup += (aTup[i],)
    return newTup

print(oddTuples(aTup))