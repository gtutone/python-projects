#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 22:12:54 2020

@author: gabrieltutone
"""

# class Primes(object):
    
#     counter = 0
#     numbers = []
#     primes = []
    
#     def __init__(self):
#         pass
        
#     def genPrimes(self):
#         while True:
#             counter =+ 1
#             numbers.append(counter)
#             yield counter
    
#     def __next__(self):

# primesNums = 0
# print(type(primesNums))
# primesNums = Primes()
# print(type(primesNums))

# primesNums.next()
import math

def genPrimes():
    counter = 2
    while True:
        isPrime = True
        
        for x in range(2, int(math.sqrt(counter) + 1)):
            if counter % x == 0:
                isPrime = False
                break
        
        if isPrime:
            yield counter
        
        counter += 1

primes = genPrimes()