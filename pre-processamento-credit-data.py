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

pd.isnull(base['age'])

base.loc[pd.isnull(base['age'])] #encontro somente os que estão nulo

#criando as duas variáveis para poder trabalhar com previsores e classe separadamente
previsores = base.iloc[:, 1:4].values
classe = base.iloc[:, 4].values

from sklearn.impute import SimpleImputer

imputer = SimpleImputer() #instancio a classe, usando os métodos padrões
imputer = imputer.fit(previsores[:, 0:3]) #para encaixar e deixar em forma
previsores[:, 0:3] = imputer.transform(previsores[:, 0:3]) #agora eu faço a mudança dos valores na coluna

