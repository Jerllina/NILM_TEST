# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:10:16 2019

@author: Jelina
"""
import pandas as pd

import matplotlib.pyplot as plt

#load data
load_information=pd.read_csv('REDD_demo_load_information.csv')

# manually specify column names
load_information.columns = ['0','P', 'Load']
load_information.drop(['0'], axis=1, inplace=True)
#split testset and trainingset
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(load_information.loc[:,load_information.columns!='Load'],
                                               load_information['Load'],stratify=load_information['Load'],random_state=66)

###k-NN test

#1.train the model
from sklearn.neighbors import KNeighborsClassifier

train_accuracy_1=[]
test_accuracy_1=[]
neighbors_settings=range(1,10)
y_predict=[]
error=[]

for n_neighbors in neighbors_settings:
    knn=KNeighborsClassifier(n_neighbors=n_neighbors)
    knn.fit(X_train,y_train)
    y_predict.append( knn.predict(X_test))
    train_accuracy_1.append(knn.score(X_train,y_train))
    test_accuracy_1.append(knn.score(X_test,y_test))

#2.visualize the results
plt.plot(neighbors_settings,train_accuracy_1,label='train accuracy')
plt.plot(neighbors_settings,test_accuracy_1,label='test accuracy')
plt.ylabel('Accuracy')
plt.xlabel('n_neighbors')
plt.legend()
plt.savefig('knn_test_model')

print('Accuracy of k-NN classifier on training set:{:.2f}'.format(knn.score(X_train,y_train)))
print('Accuracy of k-NN classifier on test set:{:.2f}'.format(knn.score(X_test,y_test)))
#print(y_predict)