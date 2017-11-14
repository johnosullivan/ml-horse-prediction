
import numpy as np
from sklearn.svm import SVC
import pandas as pd

df = pd.read_csv('data/training-2016-10-01-2016-12-31.csv')

print(df)

df['finish_pos'] = df['finish_pos'].map(lambda x: 1 if x >= 3 else 0)

print(df)
