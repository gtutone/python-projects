#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 23:11:37 2020

@author: gabrieltutone
"""


def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    
    try:
        return item / denom
        
    except ZeroDivisionError:
        return 0
        
           
print(fancy_divide([0, 2, 4], 1))