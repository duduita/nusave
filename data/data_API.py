import json
import pandas as pd
from general_info import GeneralInfo
from statistics import Statistics
from advisor import UserAdvisor


class DataAPI:
    '''
    Nao se trata bem de uma API mas sim de uma classe com uma funcao que permite acessar
    features de dados de maneira mais facil ao desenvolvedor do back
    '''

    def readInstructions(self, instruction: json):
        info = json.loads(instruction)
        feature = info['feature']
        if feature == 'statistics':
            return self.__statisticAct(info)
        if feature == 'advisor':
            return self.__advisorAct(info)

    def __statisticAct(self, info):
        stat = Statistics()
        percents = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        dict = {}
        dict["user_ID"] = info['ID']
        dict["user_last_month"] = stat.getUserLastMonth(info['ID'], info['filter'])
        dict["user_average"] = stat.getUserAverage(info['ID'], info['filter'])
        dict["category_average"] = stat.getCategoryAverage(info['ID'], info['filter'])
        percentiles = {}
        for percentage in percents:
            percentiles[percentage] = stat.getCategoryPercentiles(info['ID'],
                                                                  info['filter'], percentage / 100)
        dict["category_percentiles"] = percentiles
        return json.dumps(dict)

    def __advisorAct(self, info):
        adv = UserAdvisor()
        ID = info['ID']
        action = info['action']
        value = info['value']
        if action == 'entrada':
            instruction = ID + ',' + action + ',' + value
            return adv.readInstruction(instruction)
        if action == 'saida':
            filter = info['filter']
            instruction = ID + ',' + action + ',' + value + ',' + filter
            return adv.readInstruction(instruction)
