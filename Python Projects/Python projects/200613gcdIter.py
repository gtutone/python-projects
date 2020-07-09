#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 22:33:03 2020

@author: gabrieltutone
"""


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    gcd = a
    while gcd >= 0:
            if (b % gcd == 0) and (a % gcd == 0):
                return gcd
            else:
                gcd -= 1
                    
print(gcdIter(9, 21))