import pandas as pd
import numpy as np
from statistics import Statistics


class UserAdvisor(Statistics):
    # notice that statistics is a class(data, curr_month)

    def readInstruction(self, instruction: str):
        '''

        :param instruction: deve ser uma string que informa a ID do usuario, o tipo de
        transacao(entrada/saida), o valor e se saida deve conter o tipo de gasto
        :type instruction: string de formato 'ID,entrada,valor' ou 'ID,saida,valor,filtro'
        :return: mensagem de aviso destinada ao popup
        '''
        info = self.__decodeInstruction(instruction)
        ID = info[0]
        processo = info[1]
        valor = float(info[2])
        if processo == 'entrada':
            return self.__storingAdvice()
        elif processo == 'saida':
            filter = info[3]
            return self.__expendingAdvice(ID, valor, filter)
        else:
            return None

    def __decodeInstruction(self, instruction: str):
        return instruction.split(sep=',')

    def __storingAdvice(self):
        return None

    def __expendingAdvice(self, ID: str, valor: float, filter: str):
        mean_user = self.getUserAverage(ID, filter)
        if (valor >= 0.8 * mean_user) & (valor <= mean_user):
            percentual = 100 * valor / mean_user
            mensagem1 = 'Já foram gastos %.0f%% do valor projetado para você este ' \
                        'mês.\n' % percentual
        elif valor > mean_user:
            mensagem1 = 'Já foi gasto mais do que o esperado para você esse mês.\n'
        else:
            mensagem1 = ''
        user_category = self.__userCategory(ID)
        mean_category = self.getCategoryAverage(user_category, filter)
        if (valor >= 0.8 * mean_category) & (valor <= mean_category):
            percentual = 100 * valor / mean_category
            mensagem2 = 'Já foram gastos %.0f%% da média projetada para pessoas na ' \
                        'mesma situação que você.\n' % percentual
        elif valor > mean_user:
            mensagem2 = 'Já foi gasto mais do que a média projetada para pessoas na ' \
                        'mesma situação que você.\n'
        else:
            mensagem2 = ''
        return ('%s. ' % ID) + mensagem1 + mensagem2 + 'Verifique seus gastos e ' \
                                                       'analise se entao de acordo com os seus planos financeiros'

    def __userCategory(self, ID: str):
        #retorna uma lista em ordem protocolada das caracteristicas que compoem a
        #categoria do usuario
        user_category = []
        data_user = self.data.loc[ID]
        for category in UserAdvisor.category_list:
            user_category.append(data_user[category])
        return user_category
