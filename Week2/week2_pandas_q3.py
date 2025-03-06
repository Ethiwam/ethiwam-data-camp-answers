"""
Filename: week2_pandas_q3.py
Coder: Ethan Iwama
Purpose: Solution to Week 2 Pandas Problem 3
"""

import numpy as np
import pandas as pd

# Importing Dataset
df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))

rows_more_than_100 = df[df.sum(axis=1) > 100]

"""# Printing Tests
print(df)
print()
print(df.sum(axis=1))
print()
print(df[df.sum(axis=1) > 100])
"""