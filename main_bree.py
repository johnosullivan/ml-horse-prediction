import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn import svm, metrics, preprocessing
from sklearn.model_selection import train_test_split

#read in the data file into a pandas dataframe
data = pd.read_csv('data/training-2016-10-01-2016-12-31.csv')

#drop some features
def remove_strings(df):
    df.drop(['row_id', 'entry_id', 'morning_line'], axis=1)
    return df

data = remove_strings(data)

#our y label will be finish position, if it is in the top three (WPS)
#this function maps top three to 1 and anything other finish position to 0
def alter_y_label(df):
    df['finish_pos'] = df['finish_pos'].apply(lambda x: 1 if x >= 3 else 0)
    return df

data = alter_y_label(data)
print(data)

X = data.drop(['finish_pos'], axis=1)
y = data['finish_pos']

#sns.countplot(data['finish_pos'],label="Count")
#plt.show()

