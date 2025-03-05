"""
File Name: week1_q3.py
Coder: Ethan Iwama
Purpose: Solution to Week 1 Problem 3
"""

import re   # Need for regex splitting

string = """
I have provided this text to provide tips on creating interesting paragraphs.
First, start with a clear topic sentence that introduces the main idea.
Then, support the topic sentence with specific details, examples, and evidence.
Vary the sentence length and structure to keep the reader engaged.
Finally, end with a strong concluding sentence that summarizes the main points.
Remember, practice makes perfect!
"""

str_array = re.split(r'[ .\n!?]+', string)  # Splits string into array of words, removing punctuation
for i in range(len(str_array)):
    str_array[i] = str_array[i].lower() # All words to lowercase, so we don't separate capitalized.

word_count = {}
def word_counter(words: list, word_count: dict):
    for word in words:
        if (word == ''):    # It keeps counting '' due to how I delimited. Quick and easy fix.
            continue
        if word in word_count.keys():
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

word_counter(str_array, word_count)

for item in word_count.items():
    print(item)