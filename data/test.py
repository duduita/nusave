from data_API import DataAPI
import json
import pandas as pd
from math import inf

dataframe = pd.read_json('./monthjson/janeiro.json')
nome = dataframe['Nome'].copy()
rpg_data = pd.DataFrame(nome)
columns = ['Xp', 'Level', 'Quest']
xp_pins = [0, 50, 200, 450, 800, 1250, 1800, 2450, 3200, 4050, 5000, 6050, 7200, 8450,
           9800, 11250, 12800, 14450, 16200, 18050, inf]

for coluna in columns:




