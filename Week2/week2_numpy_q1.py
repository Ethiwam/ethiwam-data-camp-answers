"""
Filename: week2_numpy_q1.py
Coder: Ethan Iwama
Purpose: Solution to Week 2 Numpy Problem 1
"""

import numpy as np

a = np.random.random_integers(1, 101, (1,5))    # Using ints, because I felt like it   
b = np.random.random_integers(1, 101, (1,5))
new_c = np.vstack((a,b))    # Creating a vertical stacked array

d = np.random.random_integers(1, 101, (5,1))
e = np.random.random_integers(1, 101, (5,1))
new_f = np.hstack((d,e))    # Creating a horizontal stacked array

""" # For Testing
print(a)
print()
print(b)
print()
print(new_c)
print()
print('-----')
print()
print(d)
print()
print(e)
print()
print(new_f)
"""