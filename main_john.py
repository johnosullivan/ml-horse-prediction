# Imported the pandas and numpy
import numpy as np
import pandas as pd
from sklearn.svm import SVC
# Importing the sklearn library and its submodules
from sklearn.grid_search import GridSearchCV
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn import svm
from sklearn.metrics import f1_score
# Gets the data from the data folder and convert to datframes
df = pd.read_csv('data/training-2016-10-01-2016-12-31.csv')
# Gets the data we would like to use on each column
data = df.dropna(subset=['same_track','last_race_res','finish_pos'])
# Maps the finish_pos if its metals within top 3 then 1 else 0
data['finish_pos'] = data['finish_pos'].map(lambda x: 1 if x >= 3 else 0)
# Gets the y labels of the finish_pos
y_sk = data[['finish_pos']].values
# Gets the data for training 'same_track','last_race_res'
X_sk = data[['same_track','last_race_res']].values
# Gets the text/dev and training dataset / y_labels which will be splitted into dev/test
X_train, X_test_dev, y_train, y_test_dev = train_test_split(X_sk, y_sk, test_size=0.30,train_size=0.70, random_state=1)
# Reshapes the y_labels
y_test_dev_reshape = np.reshape(y_test_dev, len(y_test_dev))
# Takes X_test_dev and spliting into dev and test X/y_labels
X_dev, X_test, y_dev, y_test = train_test_split(X_test_dev, y_test_dev_reshape, test_size=0.50,train_size=0.50, random_state=1)
# Reshapes the y_labels
y_train_reshape = np.reshape(y_train, len(y_train))
y_test_reshape = np.reshape(y_test, len(y_test))
y_dev_reshape = np.reshape(y_dev, len(y_dev))
print("Tuning against the dev dataset/y_label")
param_grid = [
 {'C': [1, 10, 100, 1000], 'kernel': ['linear']},
 {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001], 'kernel': ['rbf']},
]
clfdev = svm.SVC(kernel='poly',C=2.0,random_state=2)
clfdev.fit(X_train, y_train_reshape)
c1dev = clfdev.score(X=X_dev,y=y_dev_reshape)
print("Dev Accuracy: {0:.0f}%".format(c1dev * 100))
print("Testing against best model and hyberparameters")
clf = svm.SVC(kernel='poly',C=1.0,random_state=1)
#clf = GridSearchCV(SVC(), param_grid, cv=5)
clf.fit(X_train, y_train_reshape)
#print("Best parameters set found on development set:")
#print(clf.best_params_)
c1 = clf.score(X=X_test,y=y_test_reshape)
#y_pred = clf.predict(X_test)
#print(f1_score(y_test_reshape, y_pred, average='micro'))
print("Test Accuracy: {0:.0f}%".format(c1 * 100))
