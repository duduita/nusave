import pandas as pd
import numpy as np
from math import inf


class statistics():
    month_list = ['janeiro', 'fevereiro', 'marco', 'abril',
                  'maio', 'junho', 'julho', 'agosto',
                  'setembro', 'outubro', 'novembro', 'dezembro']
    columns = ['Alimentacao', 'Assinatura_e_servicos', 'Educacao',
               'Beleza', 'Saude', 'Transporte', 'Outros', 'Saques']
    age_pins = [0, 25, 35, 50, inf]
    dependant_pins = [0, 1, 2, 3, 4, inf]

    def __init__(self, data, curr_month):
        '''

        :param data: array de DataFrames
        :param curr_month: mes atual
        '''
        self.data = data
        self.curr_index = statistics.month_list.index(curr_month)
        if (self.curr_index > 0):
            self.last_index = self.curr_index - 1
        else:
            self.last_index = 11

    def getUserLastMonth(self, user, filter):
        # retorna o os gasto total de certo usuario em certo filtro no mes passado
        return self.data[self.last_index][filter][user]

    def getUserAverage(self, user, filter):
        # retorna a media exponencial movel do usuario contabilizando 11 meses passados para certo filtro
        media = 0
        alfa = 1 / 6
        i = self.last_index

        while (i != self.curr_index):
            media = alfa * self.data[i][filter][user] + (1 - alfa) * media
            if (i > 0):
                i = i - 1
            else:
                i = 11
        return media

    def getCategoryAverage(self, category, filter):
        '''

        :param category: n-upla de strings e ints, as informacoes que definem a
        categoria devem estar na exata ordem: Classe,Regiao,Idade,Dependentes,Sexo,Estado_Civil
        :param filter: tipo de gasto
        :return: media
        '''
        # retorna a media exponencial movel da categoria  para certo filtro contabilizando 11 meses passados
        media = 0
        alfa = 1 / 6
        i = self.last_index

        while (i != self.curr_index):
            data_month = self.data[i]
            data_category = self.__getClustering(data_month, category)
            media = alfa * data_category[filter].mean() + (1 - alfa) * media
            if (i > 0):
                i = i - 1
            else:
                i = 11
        return media

    def getCategoryPercentiles(self, category, filter, quantile):
        '''

        :param category: array de strings as strings que definem a categoria devem
        estar na exata ordem: Classe,Regiao,Idade,Dependentes,Sexo,Estado_Civil
        :param filter: tipo de gasto
        :return: media
        '''
        # retorna os valores tal que desse valor para baixo estao uma fracao quantile
        # do usuarios em determinado filtro e cateogria
        media = 0
        alfa = 1 / 6
        i = self.last_index

        while (i != self.curr_index):
            data_month = self.data[i]
            data_category = self.__getClustering(data_month, category)
            media = alfa * data_category[filter].quantile(quantile) + (1 - alfa) * media
            if (i > 0):
                i = i - 1
            else:
                i = 11
        return media

    def getUserLastMonthPercentage(self, user, filter):
        # retorna a fracao de gasto de certo filtro em relacao ao total do ultimo mes
        soma = 0
        for filter in statistics.columns:
            data_expends = self.data[self.last_index][filter]
            soma = soma + data_expends[user]
        return self.data[self.last_index][filter][user] / soma

    def __getClustering(self, dataframe, category):
        data_aux = dataframe[(dataframe['Classe'] == category[0])
                             & (dataframe['Regiao'] == category[1])
                             & (dataframe['Sexo'] == category[4])
                             & (dataframe['Estado_Civil'] == category[5])
                             ]
        dep_limit = self.__setLimits(category[3], statistics.dependant_pins)
        age_limit = self.__setLimits(category[2], statistics.age_pins)

        return data_aux[(age_limit[0] <= data_aux['Idade'])
                        & (age_limit[1] > data_aux['Idade'])
                        & (dep_limit[0] <= data_aux['Dependentes'])
                        & (dep_limit[1] > data_aux['Dependentes'])
                        ]

    def __setLimits(self, value, pins):
        Pins_use = pins.copy()
        Pins_use.append(value)
        Pins_use.sort()
        limit_min = Pins_use[Pins_use.index(value) - 1]
        limit_max = Pins_use[Pins_use.index(value) + 1]
        if (value == limit_max):
            limit_min = Pins_use[Pins_use.index(value)]
            limit_max = Pins_use[Pins_use.index(value) + 2]
        return [limit_min, limit_max]
