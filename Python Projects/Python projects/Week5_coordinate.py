#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 00:28:36 2020

@author: gabrieltutone
"""

# Add an __eq__ method that returns True if coordinates refer to same point in the plane (i.e., have the same x and y coordinate).

# Define __repr__, a special method that returns a string that looks like a valid Python expression that could be used to recreate 
# an object with the same value. In other words, eval(repr(c)) == c given the definition of __eq__ from part 1.



class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        '''
        returns True if coordinates refer to same point in the plane (i.e., 
        have the same x and y coordinate)
        '''
        xEq = self.getX() == other.getX()
        yEq = self.getY() == other.getY()
        return xEq and yEq
    
    def __repr__(self):  #remove this and the next line and re-run
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'
    

c = Coordinate(1,1)

d = Coordinate(1,0)

print(c == d)
print(c)
print(eval(repr(c)))
print(eval(repr(c)) == c)