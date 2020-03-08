import pandas as pd
import numpy as np
import random as rd
from random_generator import random_generator

#--------------------------------------------------------------------
contas = pd.read_csv('example.csv', index_col=0)
print(contas)
columns = ['Alimentacao', 'Assinatura e servicos','Educacao', 'Roupas', 'Saude'
           'Transporte','Outros','Saques']
contas = random_generator(contas, columns)
#--------------------------------------------------------------------
print(contas)
contas.to_json('contas_example.json')



