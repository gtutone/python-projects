#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 22:14:47 2020

@author: gabrieltutone
"""
#from time import sleep
balance = 4773
annualInterestRate = 0.2

import math
def roundup(x):
    return int(math.ceil(x / 10.0)) * 10
monthlyInterest = annualInterestRate / 12.0
low = balance / 12
high = (balance * (1 + monthlyInterest)**12)/12
fixMonthlyPay = (low + high)/2
epsilon = 0.01

def FixedMonthly(balance, annualInterestRate, fixMonthlyPay, months, low, high):
    balanceCheck = 0
    def RemBalance(balance, annualInterestRate, fixMonthlyPay, months):
        monthlyInterest = annualInterestRate / 12.0
        monthlyUnpaid = balance - fixMonthlyPay
        balance = monthlyUnpaid + (monthlyInterest * monthlyUnpaid)   
        if months == 1 or balance <= 0:
            return balance
        else:
            return RemBalance(balance, annualInterestRate, fixMonthlyPay, months - 1)

#    print("High is", high, ", low is", low, "and payment is", fixMonthlyPay); sleep(0.5)
    balanceCheck = RemBalance(balance, annualInterestRate, fixMonthlyPay, 12)
    
    if high - low <= epsilon:
        return fixMonthlyPay
    if balanceCheck < 0:
        high = fixMonthlyPay
        fixMonthlyPay = (low + high)/2
        return FixedMonthly(balance, annualInterestRate, fixMonthlyPay, months, low, high)
    elif balanceCheck > 0:
        low = fixMonthlyPay
        fixMonthlyPay = (low + high)/2
        return FixedMonthly(balance, annualInterestRate, fixMonthlyPay, months, low, high)
    else:
        return fixMonthlyPay

print("Lowest Payment:", roundup(((FixedMonthly(balance, annualInterestRate, fixMonthlyPay, 12, low, high)))))