#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 22:07:41 2020

@author: gabrieltutone
"""

s = "azcbobobegghbakolb"
bob = "bob"
indexCount = 0
bobTemp = ""
numBobs = 0

for i in s:
    if i in bob:
        bobTemp = s[indexCount:indexCount+3]
        if bobTemp == bob:
            numBobs +=1
    indexCount += 1

print("Number of times bob occurs is: " + str(numBobs))