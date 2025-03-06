"""
Filename: week2_optional.py
Coder: Ethan Iwama
Purpose: Solution to Week 2 Optional Problem
"""

## Optional Practice Question

#Find the mean of a numeric column grouped by a categorical column in a 2D numpy array

import numpy as np
import statistics

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')


numeric_column = iris[:, 1].astype('float')  # sepalwidth
grouping_column = iris[:, 4]  # species

output = []
num_setosa = np.where(iris[:,4] == b'Iris-setosa')  # These find which rows belong to which species
num_versicolor = np.where(iris[:,4] == b'Iris-versicolor')
num_virginica = np.where(iris[:,4] == b'Iris-virginica')

# Getting mean for setosas
setosa_column = iris[num_setosa[0][0]:num_setosa[0][-1], 1].astype('float')
output.append(statistics.mean(setosa_column))

# Getting mean for versicolors
versicolor_column = iris[num_versicolor[0][0]:num_versicolor[0][-1], 1].astype('float')
output.append(statistics.mean(versicolor_column))

# Getting mean for virginicas
virginica_column = iris[num_virginica[0][0]:num_virginica[0][-1], 1].astype('float')
output.append(statistics.mean(virginica_column))

output