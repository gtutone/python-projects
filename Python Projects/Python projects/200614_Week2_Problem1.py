#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 21:35:46 2020

@author: gabrieltutone
"""


balance = 42                # Outstanding balance on credit card
annualInterestRate = 0.2    # annual interest rate as a decimal
monthlyPaymentRate = 0.04   # minimum monthly payment rate as a decimal

def RemBalance(balance, annualInterestRate, monthlyPaymentRate, months):
    monthlyInterest = annualInterestRate / 12.0
    minMonthlyPay = monthlyPaymentRate * balance
    monthlyUnpaid = balance - minMonthlyPay
    balance = monthlyUnpaid + (monthlyInterest * monthlyUnpaid)
    
    if months == 0:
        return round(balance, 2)
    
    else:
#        monthPrint = 1
#        print("Month", monthPrint, "Remaining balance:", round(balance, 2))
#        monthPrint += 1
        return RemBalance(balance, annualInterestRate, monthlyPaymentRate, months - 1)


print("Remining balance:", RemBalance(balance, annualInterestRate, monthlyPaymentRate, 11))