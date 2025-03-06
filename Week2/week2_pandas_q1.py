"""
Filename: week2_pandas_q1.py
Coder: Ethan Iwama
Purpose: Solution to Week 2 Pandas Problem 1
"""

import numpy as np
import pandas as pd

# Importing Dataset
df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')

df_filtered = df.loc[df.index[::20], ['Manufacturer', 'Model', 'Type']]

print(df_filtered)