# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 20:45:09 2021

@author: welli
"""
import pandas as pd
base = pd.read_csv('credit_data.csv')

base.describe()

base.loc[base['age'] < 0]
# apagar a coluna
base.drop('age', 1, inplace=True)
# apagar somente os registros inconsistentes
base.drop(base[base.age < 0].index, inplace=True)
# preencher os valores manualmente (em caso de uma base pequena)

# preencher os valores com a média (ideal)
base.mean() #vejo a média de todos as colunas do meu dataframe
base['age'].mean() #essa média ainda não corresponde a verdade, pois tem as idades inconsistentes
base['age'][base.age > 0].mean() #encontro a média retirando os negativos
base.loc[base.age < 0, 'age'] = 40.92 #insiro a média correta nas idades negativas
