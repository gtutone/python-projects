#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 11:53:11 2020

@author: gabrieltutone
"""


def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    Inc = []
    Dec = []
    LongInc = [] # To store longest increasing monotonic list
    LongDec = [] # To store longest decreasing monotonic list
    
    if L[0] >= L[1]:
        Dec.append(L[0])
    else:
        Inc.append(L[0])
    
    print('Inc is:', Inc, 'Dec is:', Dec)
    print('Long record is:', LongInc, 'Dec record is:', LongDec)

    
    for i in range(len(L)-1):
        # Check if next int is biggerm equal or smaller
        
        # If next int is bigger
        if L[i] < L[i+1]:
            # Append int to Increasing list
            Inc.append(L[i+1])
            # If Decreasing hasn't been emptied, append previous number
            # if Dec != []:
            #     Inc.append(L[i])
            # Empty out Decreasing streak
            Dec = []
            # Check if Increasing list beats record
            if len(Inc) > len(LongInc):
                LongInc = Inc[:]

        # If next int is smaller
        elif L[i] > L[i+1]:
            #Empty out the Increasing streak
            Inc = []
            # Append int to Decreasing list
            Dec.append(L[i+1])
            # Check whether decreasing list beats the record
            if len(Dec) > len(LongDec):
                LongDec = Dec[:]
        
        # If it's equal, add to both lists and increase record lists
        else:
            Inc.append(L[i])
            if len(Inc) > len(LongInc):
                LongInc = Inc[:]
            Dec.append(L[i])            
            if len(Dec) > len(LongDec):
                LongDec = Dec[:]

        print('Inc is:', Inc, 'Dec is:', Dec)
        print('Long record is:', LongInc, 'Dec record is:', LongDec)
    
    if LongInc >= LongDec:
        return sum(LongInc, 0)
    else:
        return sum(LongDec, 0)


L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]
print(longest_run(L))