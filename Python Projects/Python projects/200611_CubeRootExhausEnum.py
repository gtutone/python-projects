#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 21:49:04 2020

@author: gabrieltutone
"""


cube = 29
epsilon = 0.1
guess = 0.0
increment = 0.001
num_guesses = 0

while abs(guess**3 - cube) >= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print("num_guesses,", num_guesses)
if abs(guess**3 - cube) > epsilon:
    print("Failed on cube root of ", str(cube))
else:
    print(str(guess), "is close to the cube root of", str(cube))