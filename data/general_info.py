from math import inf
from pandas import pd


class GeneralInfo():
    month_list = ['janeiro', 'fevereiro', 'marco', 'abril',
                  'maio', 'junho', 'julho', 'agosto',
                  'setembro', 'outubro', 'novembro', 'dezembro']
    filter_list = ['Alimentacao', 'Assinatura_e_servicos', 'Educacao',
                   'Beleza', 'Saude', 'Transporte', 'Outros', 'Saques']
    category_list = ['Classe','Regiao','Idade','Dependentes','Sexo','Estado_Civil']
    info_list = ['Entrada', 'Saldo']
    age_pins = [0, 25, 35, 50, inf]
    dependant_pins = [0, 1, 2, 3, 4, inf]

    def __init__(self):
        data = []
        for month in GeneralInfo.month_list:
            dataframe = pd.read_json('./monthjson/'+month + '.json')
            data.append(dataframe)
        self.data = data
        curr_month = pd.read_json('curr_month')
        self.curr_month = curr_month

    def __userCategory(self, ID: str):
        #retorna uma lista em ordem protocolada das caracteristicas que compoem a
        #categoria do usuario
        user_category = []
        data_user = self.data[0].loc[ID]
        for category in GeneralInfo.category_list:
            user_category.append(data_user[category])
        return user_category
