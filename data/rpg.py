from statistics import Statistics


class RPGFrame(Statistics):
    level_pins = []

    def __init__():
        super(RPGFrame, self).__init__(data, curr_month)
        self.rpg_data = rpg_data

    def updateRPG(self, ID):

    def __updateQuest(self, ID):
        if(self.__wasSuccessful(ID)):
            self.rpg_data['Xp'][ID] = self.rpg_data['Xp'][ID] + 50


    def __wasSuccessful(self, ID):
        aux_data = self.data[self.curr_index].loc[ID]
        aux2_data = self.data[self.last_index].loc[ID]
        stored = ((aux_data['Saldo'] + aux_data['Saques'])
                  - (aux2_data['Saldo'] + aux2_data['Saques']))
        quest_value = self.rpg_data['Quest'][ID]
        return stored > quest_value
