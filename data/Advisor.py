import pandas as pd
import numpy as np
from statistics import statistics

class advisor(statistics):
    # notice that statistics is a class(data, curr_month)
    def readInformation(self, info):
        '''

        :param info: deve ser uma string que informa a ID do usuario, o tipo de
        transacao(entrada/saida), se saida deve conter o tipo de gasto
        :type info: string de formato 'ID,entrada' ou 'ID,saida,filtro'
        '''
        


