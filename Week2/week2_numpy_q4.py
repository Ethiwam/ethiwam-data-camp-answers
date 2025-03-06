"""
Filename: week2_numpy_q4.py
Coder: Ethan Iwama
Purpose: Solution to Week 2 Numpy Problem 4
"""

import numpy as np

# Importing Iris Dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])

indices = np.where((iris_2d[:,2] > 1.5) & (iris_2d[:,0] < 5.0))
filtered_iris = iris_2d[indices]

print(iris_2d)
print()
print(filtered_iris)