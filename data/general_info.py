from math import inf
import pandas as pd


class GeneralInfo():
    month_list = ['janeiro', 'fevereiro', 'marco', 'abril',
                  'maio', 'junho', 'julho', 'agosto',
                  'setembro', 'outubro', 'novembro', 'dezembro']
    filter_list = ['Alimentacao', 'Assinatura_e_servicos', 'Educacao',
                   'Beleza', 'Saude', 'Transporte', 'Outros', 'Saques']
    category_list = ['Classe','Regiao','Idade','Dependentes','Sexo','Estado_Civil']
    info_list = ['Entrada', 'Saldo']
    age_pins = [-1, 25, 35, 50, inf]
    dependant_pins = [-1, 1, 2, 3, 4, inf]
    xp_pins = [-1, 50, 200, 450, 800, 1250, 1800, 2450, 3200, 4050, 5000, 6050, 7200, 8450,
               9800, 11250, 12800, 14450, 16200, 18050, inf]

    def __init__(self):
        data = []
        for month in GeneralInfo.month_list:
            dataframe = pd.read_json('./monthjson/'+month + '.json')
            dataframe.set_index(inplace=True, keys='Nome')
            data.append(dataframe)
        self.data = data
        curr_month = pd.read_json('curr_month.json')
        self.curr_month = curr_month['month'][0]

    def _userCategory(self, ID: str):
        #retorna uma lista em ordem protocolada das caracteristicas que compoem a
        #categoria do usuario
        user_category = []
        data_user = self.data[0].loc[ID]
        for category in GeneralInfo.category_list:
            user_category.append(data_user[category])
        return user_category
