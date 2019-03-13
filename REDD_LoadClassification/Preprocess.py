# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 08:37:55 2019

@author: Jelina

"""

import pandas as pd
import numpy as np

###read House1 data for training
dataset=pd.read_csv('House1.csv')
'''
#print(dataset.columns)
Index(['datetime', 'mains_1', 'mains_2', 'oven_3', 'oven_4', 'refrigerator_5',
       'dishwaser_6', 'kitchen_outlets_7', 'kitchen_outlets_8', 'lighting_9',
       'washer_dryer_10', 'microwave_11', 'bathroom_gfi_12',
       'electric_heat_13', 'stove_14', 'kitchen_outlets_15',
       'kitchen_outlets_16', 'lighting_17', 'lighting_18', 'washer_dryer_19',
       'washer_dryer_20'],
      dtype='object')
'''

###preprocess

"""
Labels:
    1.datetime 时间戳
    2.mains_1 主表1
    3.mains_2  主表2
    4.P  有功功率
    5.Load 负荷类型
"""

#manually drop the data we do not need in this stage
dataset.drop(['datetime', 'mains_1', 'mains_2'], axis=1, inplace=True)

#split and save data for some loads. 
t1=pd.DataFrame((dataset['oven_3'])[dataset.oven_3!= 0])
t1=t1.stack().reset_index(level=0).rename(columns={0:'P'})
t1.drop(['level_0'], axis=1, inplace=True)
t1['Load'] = 'oven'
t1.to_csv('oven_1_information.csv')

t2=pd.DataFrame((dataset['oven_4'])[dataset.oven_4!= 0])
t2=t2.stack().reset_index(level=0).rename(columns={0:'P'})
t2.drop(['level_0'], axis=1, inplace=True)
t2['Load'] = 'oven'
t2.to_csv('oven_2_information.csv')

t3=pd.DataFrame((dataset['dishwaser_6'])[dataset.dishwaser_6!= 0])
t3=t3.stack().reset_index(level=0).rename(columns={0:'P'})
t3.drop(['level_0'], axis=1, inplace=True)
t3['Load'] = 'dishwaser'
t3.to_csv('dishwaser_information.csv')

t4=pd.DataFrame((dataset['refrigerator_5'])[dataset.refrigerator_5!= 0])
t4=t4.stack().reset_index(level=0).rename(columns={0:'P'})
t4.drop(['level_0'], axis=1, inplace=True)
t4['Load'] = 'refrigerator'
t4.to_csv('refrigerator_information.csv')

t5=pd.DataFrame((dataset['lighting_9'])[dataset.lighting_9!= 0])
t5=t5.stack().reset_index(level=0).rename(columns={0:'P'})
t5.drop(['level_0'], axis=1, inplace=True)
t5['Load'] = 'lighting'
t5.to_csv('lighting_information.csv')

t6=pd.DataFrame((dataset['microwave_11'])[dataset.microwave_11!= 0])
t6=t6.stack().reset_index(level=0).rename(columns={0:'P'})
t6.drop(['level_0'], axis=1, inplace=True)
t6['Load'] = 'microwave'
t6.to_csv('microwave_information.csv')

#t_sum=pd.concat([t1,t2,t3,t4,t5,t6],axis=0)
#t_sum.to_csv('REDD_load_information.csv')

t_demo=pd.concat([t1[:1000],t2[:1000],t3[:1000],t4[:1000],t5[:1000],t6[:1000]],axis=0)
t_demo.to_csv('REDD_demo_load_information.csv')