#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 00:18:58 2020

@author: gabrieltutone
"""
balance = 4773
annualInterestRate = 0.2
monthlyInterest = annualInterestRate / 12.0
low = balance / 12
high = (balance * (1 + monthlyInterest)**12)/12
fixMonthlyPay = 434.89687662627284


def RemBalance(balance, annualInterestRate, fixMonthlyPay, months):
    monthlyInterest = annualInterestRate / 12.0
    monthlyUnpaid = balance - fixMonthlyPay
    balance = monthlyUnpaid + (monthlyInterest * monthlyUnpaid)   
    if months == 1 or balance <=0:
        return balance
    else:
        return RemBalance(balance, annualInterestRate, fixMonthlyPay, months - 1)
    
print("Remianing balance is", RemBalance(balance, annualInterestRate, fixMonthlyPay, 12))