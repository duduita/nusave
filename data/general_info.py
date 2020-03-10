from math import inf


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

    def __init__(self, data):
        self.data = data

    def __userCategory(self, ID: str):
        #retorna uma lista em ordem protocolada das caracteristicas que compoem a
        #categoria do usuario
        user_category = []
        data_user = self.data.loc[ID]
        for category in GeneralInfo.category_list:
            user_category.append(data_user[category])
        return user_category
