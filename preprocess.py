# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 20:37:27 2019

@author: Jelina
"""

import pandas as pd

#read the whole dataset  
dataset = pd.read_csv("House1.csv")

#get the load types
loadlist=dataset.columns.tolist()


col0=pd.DataFrame(dataset[loadlist[0]])
col1=pd.DataFrame(dataset[loadlist[1]])
col2=pd.DataFrame(dataset[loadlist[2]])

dataset_head=col0
dataset_head[loadlist[1]]=col1
dataset_head[loadlist[2]]=col2


'''Read different loads into individual datasets.'''
for i in range(3,21): 
    dataset_i=pd.DataFrame(dataset_head)
    dataset_i.append(dataset_head)
    col_name=loadlist[i]
    new_col=pd.DataFrame(dataset[col_name])
    dataset_i[col_name]=new_col
    dataset_i.to_csv('{0}.csv'.format(col_name))
    