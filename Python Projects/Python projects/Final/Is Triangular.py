#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 11:15:05 2020

@author: gabrieltutone
"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    A triangular number is a number obtained by the continued summation of 
    integers starting from 1.
    For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 
    1, 3, 6, 10, etc., are triangular numbers.
    """
    y = 1
    x = 1
    while x <= k:
        # If x equals k, it must be triangular
        if k == x:
            return True
        
        else:
            y += 1
            x = x + y
    
    return False

print(is_triangular(10))