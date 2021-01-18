# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:00:01 2021

@author: RECEPÇÃO
"""

import pandas as pd
base = pd.read_csv('census.csv')

previsores = base.iloc[:, 0:14].values
classe = base.iloc[:, 14].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder #transformando 'work class' de atributo nominal para
#numerico
from sklearn.compose import ColumnTransformer
labelencoder_previsores = LabelEncoder() #instanciando
#faça a mudança para todas as colunas que estão com atributo nominal para númerico e assim poder --
#fazer o treinamento corretamente
previsores[:, 1] = labelencoder_previsores.fit_transform(previsores[:, 1])
previsores[:, 3] = labelencoder_previsores.fit_transform(previsores[:, 3])
previsores[:, 5] = labelencoder_previsores.fit_transform(previsores[:, 5])
previsores[:, 6] = labelencoder_previsores.fit_transform(previsores[:, 6])
previsores[:, 7] = labelencoder_previsores.fit_transform(previsores[:, 7])
previsores[:, 8] = labelencoder_previsores.fit_transform(previsores[:, 8])
previsores[:, 9] = labelencoder_previsores.fit_transform(previsores[:, 9])
previsores[:, 13] = labelencoder_previsores.fit_transform(previsores[:, 13])

#usando variáveis 'dummy' para o gênero
#feito as mudanças na variável de previsores nas colunas que precisavam
onehotencoder = ColumnTransformer(transformers=[("OneHot", OneHotEncoder(), [1,3,5,6,7,8,9,13])],remainder='passthrough')
previsores = onehotencoder.fit_transform(previsores).toarray()

#agora mudando para atributo númerico a variável classe
labelencoder_classe = LabelEncoder()
classe = labelencoder_classe.fit_transform(classe)

#fazendo o escalonamento dos valores
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(previsores)
