import pandas as pd
from __random_generator import random_generator
from statistics import statistics

#--------------------------------------------------------------------

contas = pd.read_csv('__example.csv', index_col=0)
print(contas)
columns = ['Alimentacao', 'Assinatura_e_servicos','Educacao', 'Beleza', 'Saude'
           'Transporte','Outros','Saques']
category = ['A', 'metropolitana', '50+', '4+ filhos', 'mulher', 'solteiro']
data = []
for i in range(0,12):
    data.append(contas)
    random_generator(data[i], columns)

contas.to_json('contas_exemple.json')










