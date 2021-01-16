# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 20:45:09 2021

@author: welli
"""
import pandas as pd
base = pd.read_csv('credit_data.csv')
base.describe()

base.loc[base['age'] < 0]
