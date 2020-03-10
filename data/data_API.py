import json
import pandas as pd
from general_info import GeneralInfo
from statistics import Statistics
from advisor import UserAdvisor


class DataAPI:

    def ReadInstructions(self, instruction: json):
        info = json.loads(instruction)
        feature = info['feature']
        if feature == 'statistics':
            return self.__statisticAct(info)
        if feature == 'advisor':
            return self.__advisorAct(info)



    def __statisticAct(self, info):
        stat = Statistics()
        request = info['request']
        if request == 'get_user_last_month':
            return stat.getUserLastMonth(info['ID'], info['filter'])
        if request == 'get_user_average':
            return stat.getUserAverage(info['ID'], info['filter'])
        if request == 'get_category_average':
            return stat.getCategoryAverage(info['ID'], info['filter'])
        if request == 'get_category_percentiles':
            return stat.getCategoryPercentiles(info['ID'], info['filter'])

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

