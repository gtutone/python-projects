#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 22:07:41 2020

@author: gabrieltutone
"""
x = int(input("Type a number: "))

if x%2 == 0:
    if x%3 == 0:
        print("Divisible by 2 and 3")
    else:
        print("Divisible by 2 and not 3")
elif x%3 ==0:
    print("Divisible by 3, not by 2")
else:
    print("Not divisible by 2 and 3")5