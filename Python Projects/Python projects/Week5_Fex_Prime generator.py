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




def genPrimes():
    primes = [2]
    counter = 1
    while True:
        counter += 1
        for x in primes:
            if counter % x != 0:
                primes.append(counter)
                yield counter


primes = genPrimes()