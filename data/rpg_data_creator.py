from data/data_API import DataAPI
import json
import random as rd
import pandas as pd
from math import inf

dataframe = pd.read_json('./monthjson/janeiro.json')
nome = dataframe['Nome'].copy()
n = dataframe.shape[0]

columns = ['Xp', 'Level', 'Quest']
xp_pins = [-1, 50, 200, 450, 800, 1250, 1800, 2450, 3200, 4050, 5000, 6050, 7200, 8450,
           9800, 11250, 12800, 14450, 16200, 18050, inf]

xp = []
level = []
quest = []

for i in range(0, n):
    xp.append(rd.randint(0, 10000))
    level.append(0)
    quest.append(0)
frame = {'Xp': xp, 'Level': level, 'Quest': quest}
rpg_data = pd.DataFrame(frame)

rpg_data["Nome"] = nome
rpg_data.set_index('Nome')

rpg_data.to_json('rpg_data.json')

print(rpg_data)







