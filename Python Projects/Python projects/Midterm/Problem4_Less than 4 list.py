#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 11:56:43 2020

@author: gabrieltutone
"""


aList = ["apple", "321", "1", "ban321321321ana", ""]

bList = ["12345"]

cList = []

dList = ["123"]


def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    FourList = []
    
    for i in aList:
        if len(i) < 4:
            FourList.append(i)
        #print(FourList)
    
    return FourList
    

print(lessThan4(aList))

print(lessThan4(bList))

print(lessThan4(cList))

print(lessThan4(dList))
