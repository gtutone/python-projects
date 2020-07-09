#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 12:46:03 2020

@author: gabrieltutone
"""

#from time import sleep

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    
    if N == 0:
        return N
    
    else:
        return (N % 10) + sumDigits(N // 10)

print(sumDigits(126349999999))