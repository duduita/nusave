import pandas as pd
from __random_generator import random_generator
from statistics import statistics

#--------------------------------------------------------------------

contas = pd.read_csv('__example.csv', index_col=0)
columns = ['Alimentacao', 'Assinatura_e_servicos','Educacao', 'Beleza', 'Saude'
           'Transporte','Outros','Saques']
category = ('A', 'metropolitana', 30, 4, 'feminino', 'solteiro')
data = []
for i in range(0,12):
    data.append(contas)
    random_generator(data[i], columns)

stat = statistics(data,'fevereiro')
print(data[0])

print(stat.getCategoryAverage(category, 'Beleza'))
#-------------------------------------------------------












