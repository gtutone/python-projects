#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 22:07:41 2020

@author: gabrieltutone
"""

s = "azcbobobegghakl"
vowels = "aeiou"
numVow = 0

for i in s:
    if i in vowels:
        numVow += 1
print("Number of vowels: " + str(numVow))