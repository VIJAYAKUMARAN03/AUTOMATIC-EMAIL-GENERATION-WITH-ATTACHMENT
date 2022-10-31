# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 22:06:56 2022

@author: DELL
"""

import pandas as pd
def names():
    data = pd.read_csv('dd.csv')
    l1=list(data['id'])
    l2=list(data['name'])
    l=[]
    for i in range(len(l1)):
        l.append([l1[i],l2[i]])
    return l
