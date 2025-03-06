"""
Filename: week2_numpy_q2.py
Coder: Ethan Iwama
Purpose: Solution to Week 2 Numpy Problem 2
"""

import numpy as np

a = np.array([3, 6, 9, 12]) # Test Arrays to use
b = np.array([6, 12, 18, 24])

c = np.intersect1d(a,b)

print(c)