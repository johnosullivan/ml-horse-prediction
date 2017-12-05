import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

# read in the data file into a pandas dataframe
data = pd.read_csv('data/training-2016-10-01-2016-12-31.csv')

# drop some features
def remove_strings(df):
    df= df.drop(['row_id', 'entry_id', 'morning_line'], axis=1)
    return df


# our y label will be finish position, if it is in the top three (WPS)
# this function maps top three to 1 and anything other finish position to 0
def alter_y_label(df):
    df['finish_pos'] = df['finish_pos'].apply(lambda x: 1 if x >= 3 else 0)
    return df

# Apply functions to the data
data = remove_strings(data)
data = alter_y_label(data)

# Sort dataframe into X and y variables
X = data.drop(['finish_pos'], axis=1)
y = data['finish_pos']

# Transform X and y variables into np arrays
X_all = np.array(X.iloc[0:95518, 0:25].values)
y_all = np.array(data['finish_pos'])

# Divide into train, dev, and test sets
X_train, X_dev_test, y_train, y_dev_test = train_test_split(X_all, y_all, test_size=0.30, random_state=1)
y_temp = np.reshape(y_dev_test, len(y_dev_test))
X_test, X_dev, y_test, y_dev = train_test_split(X_dev_test, y_temp, test_size=0.50, random_state=1)

# create the knn classifier
# I ran a grid search, found 7 to be the highest performing hyperparameter
knn = KNeighborsClassifier(n_neighbors=7)
knn.fit(X_train, y_train)

# predict on development
predictions = knn.predict(X_dev)
expectations = y_dev

# print performance metric score
print(metrics.f1_score(expectations, predictions))