"""
File Name: week1_q6.py
Coder: Ethan Iwama
Purpose: Solution to Week 1 Problem 6
"""

for i in range(20): # Iterate from 0-19
    num = i + 1
    if (num % 2 == 0):    # Checks if even
        print(str(num) + ', even')
    else:
        print(str(num) + ', odd')