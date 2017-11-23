import numpy as np 
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier #imports the dtree classifier
from sklearn.metrics import accuracy_score #using accuracy to rate the model
from sklearn import tree

df=pd.read_csv('data/training-2016-10-01-2016-12-31.csv') #Reads the dataset... Used the same one as John

print('Dataset Shape::',df.shape) #prints the length of the dataset...
print('Dataset Lenght::', len(df)) #prints the shape of the dataset...

print('Dataset::' , df.head()) #prints the column heads...

print(df.dtypes) #Prints the type of data...

X = df.values[:,3:24] #X is everything else besides the first two columns and the last one, removed the -1
Y= df.values[:,25] #Y is the finishing Postion 

X_train, X_test, y_train , y_test = train_test_split(X,Y, test_size=0.30,train_size=0.70, random_state=1) #split 30:70

clf_gini = DecisionTreeClassifier(criterion="gini", random_state = 100, max_depth=10, min_samples_leaf=5) #dtree with criterion gini index

clf_gini.fit(X_train, y_train)


#Uncomment this when I get there...
# print("Accuracy is", accuracy_score(y_test,y_pred)*100) # Prints accuracy score with criterion as gini index
# print("Accuracy is", accuracy_score(y_test,y_pred_en)*100)#Prints accuracy score with criterion as information gain
