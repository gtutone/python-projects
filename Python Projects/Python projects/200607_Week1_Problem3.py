#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 22:07:41 2020

@author: gabrieltutone
"""
s = "qgqgfarcmnryxdffpe"
#s = "zyxwvutsrqponmlkjihgfedcba"

alphabet = "abcdefghijklmnopqrstuvwxyz"
AlphaStr = ""
LongAlphaStr = ""

for i in range(0, (len(s)-1)):
    if s[i] <= s[i+1]:      # Check if current letter precedes or is equal to next one
        AlphaStr = AlphaStr[:-1]    # Remove repeated letter
        AlphaStr += (s[i] + s[i+1])     # Add current and next letter
        if len(AlphaStr) > len(LongAlphaStr):  # Check if current string is longer than longest alphabetical string
            LongAlphaStr = AlphaStr
    elif s[i] > s[i+1]:
            AlphaStr = ""

if LongAlphaStr == "":
    LongAlphaStr = s[0]

print("Longest substring in alphabetical order is: " + LongAlphaStr)