"""
Filename: week2_pandas_q2.py
Coder: Ethan Iwama
Purpose: Solution to Week 2 Pandas Problem 2
"""

import numpy as np
import pandas as pd

# Importing Dataset
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

df[df['Min.Price'] != df['Min.Price']] = df['Min.Price'].mean() # NaN vals aren't equal to themselves
df[df['Max.Price'] != df['Max.Price']] = df['Max.Price'].mean()

"""# Test Prints
print(df[df['Min.Price'] != df['Min.Price']])
print()
print(df[df['Max.Price'] != df['Max.Price']])
"""