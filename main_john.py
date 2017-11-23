
import numpy as np
from sklearn.svm import SVC
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.colors import ListedColormap
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from numpy.random import seed
from sklearn import svm

df = pd.read_csv('data/training-2016-10-01-2016-12-31.csv')

data = df.dropna(subset=['same_track','last_race_res','finish_pos'])

data['finish_pos'] = data['finish_pos'].map(lambda x: 1 if x >= 3 else 0)

y_sk = data[['finish_pos']].values

X_sk = data[['same_track','last_race_res']].values

X_train, X_test_dev, y_train, y_test_dev = train_test_split(X_sk, y_sk, test_size=0.30,train_size=0.70, random_state=1)

y_test_dev_reshape = np.reshape(y_test_dev, len(y_test_dev))

X_dev, X_test, y_dev, y_test = train_test_split(X_test_dev, y_test_dev_reshape, test_size=0.30,train_size=0.70, random_state=1)

y_train_reshape = np.reshape(y_train, len(y_train))

clf = svm.SVC(kernel='poly',C=1.5,random_state=1)

clf.fit(X_train, y_train)

c1 = clf.score(X=X_test,y=y_test)

print("Accuracy: {0:.0f}%".format(c1 * 100))
