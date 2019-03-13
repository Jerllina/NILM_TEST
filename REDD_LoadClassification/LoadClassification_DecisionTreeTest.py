# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:48:37 2019

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

###DecisionTree Test


#1.train the model
from sklearn.tree import DecisionTreeClassifier

train_accuracy_2=[]
test_accuracy_2=[]
depth_settings=range(1,9)

for max_depth in depth_settings:
    tree=DecisionTreeClassifier(max_depth=max_depth,random_state=0)
    tree.fit(X_train,y_train)
    
    train_accuracy_2.append(tree.score(X_train,y_train))
    test_accuracy_2.append(tree.score(X_test,y_test))

#2.visualize the results
plt.plot(depth_settings,train_accuracy_2,label='train accuracy')
plt.plot(depth_settings,test_accuracy_2,label='test accuracy')
plt.ylabel('Accuracy')
plt.xlabel('max_depth')
plt.legend()
plt.savefig('tree_test_model')

print('Accuracy of DecisionTree classifier on training set:{:.2f}'.format(tree.score(X_train,y_train)))
print('Accuracy of DecisionTree classifier on test set:{:.2f}'.format(tree.score(X_test,y_test)))

#3.visualize feature importance
print('Feature importances:\n{}'.format(tree.feature_importances_))