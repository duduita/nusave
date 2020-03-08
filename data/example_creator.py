import pandas as pd
import numpy as np
import random as rd
from random_generator import random_generator
from statistics import statistics

#--------------------------------------------------------------------

contas = pd.read_csv('example.csv', index_col=0)
columns = ['Alimentacao', 'Assinatura e servicos','Educacao', 'Roupas', 'Saude'
           'Transporte','Outros','Saques']
category = ['A', 'metropolitana', '50+', '4+ filhos', 'mulher']
data = []
for i in range(0,12):
    data.append(contas)
    random_generator(data[i], columns)

print(data[1]['Alimentacao':'Saques']['Paulo'].sum())








