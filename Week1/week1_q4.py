"""
File Name: week1_q4.py
Coder: Ethan Iwama
Purpose: Solution to Week 1 Problem 4
"""
def count_vowels(word: str):
    vowels = ['a','e','i','o','u']
    count = 0

    for letter in word:
        if letter.lower() in vowels:    # lowercase to catch all vowels
            count = count + 1
    
    return count