"""
Filename: week2_numpy_q3.py
Coder: Ethan Iwama
Purpose: Solution to Week 2 Numpy Problem 3
"""

import numpy as np

a = np.random.randint(-5, 20, (1, 5))

indices = np.where((a >= 5) & (a <= 10))
extracted_a = a[indices]

print(a)
print()
print(extracted_a)