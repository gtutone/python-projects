# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

low = 0
high = 100
ans = int((high + low) / 2)
guess = ""

print("Please think of a number between 0 and 100!")
while ans >= 0:
    print("Is your secret number " + str(ans) + "?")
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if guess == "l":
        low = ans
        ans = int((high + low) / 2)
    elif guess == "h":
        high = ans
        ans = int((high + low) / 2)
    elif guess == "c":
        break
    else:
        print("Sorry, I did not understand your input.")
    

print("Game over. Your secret number was:", ans)