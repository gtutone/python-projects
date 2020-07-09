#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 07:28:05 2020

@author: gabrieltutone
"""


import math

def polysum(n, s):
    '''
    Formulas
    ----------
    The area of regular polygon is: (0.25*n*s^2)/tan(pi/n)
    The perimeter of a polygon is: length of the boundary of the polygon

    Parameters
    ----------
    n : number of sided of polygon
    s : length of each side

    Returns
    -------
    The function returns the sum of the area and square of the perimeter of the 
    regular polygon, rounded to 4 decimal places.

    '''
    return round(((0.25 * n * s**2)/math.tan(math.pi/n)) + ((n * s) ** 2), 4)

# Function test
Answer1 = 1109972.9891
Test1 = polysum(78, 13)
if Test1 == Answer1:
    print('Success')
else:
    print('Incorrect, returns', Test1, 'instead of', Answer1)