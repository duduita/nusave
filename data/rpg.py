from statistics import Statistics
import pandas as pd

class RPGFrame(Statistics):

    def __init__(self):
        super().__init__()
        self.rpg_data = pd.read_json('rpg_data.json')
        self.rpg_data.set_index('Nome', inplace=True)

    def updateRPG(self):
        self.__updateLevel()
        self.rpg_data.reset_index(inplace=True)
        #qualquer dataset armazenado em um json file tem que esta com a indexacao nativa(numerica)
        self.rpg_data.to_json('rpg_data.json')
        self.rpg_data.set_index('Nome', inplace=True)
        
    def userRPGInfo(self, ID):
        ''':return DataFrame'''
        return self.rpg_data.loc[ID]


    def __updateLevel(self):
        #da reward
        #atualiza os niveis
        #atualiza as missoes mensais
        for ID in self.rpg_data['Nome']:
            if(self.__wasSuccessful(ID)):
                self.rpg_data['Xp'][ID] = self.rpg_data['Xp'][ID] + 50
                self.rpg_data['Level'][ID] = self.__userLevel(ID)
        self.rpg_data['Quest'] = self.rpg_data['Level'].apply(self.__questValue)


    def __wasUserSuccessful(self, ID):
        aux_data = self.data[self.curr_index].loc[ID]
        aux2_data = self.data[self.last_index].loc[ID]
        stored = ((aux_data['Saldo'] + aux_data['Saques'])
                  - (aux2_data['Saldo'] + aux2_data['Saques']))
        quest_value = self.rpg_data['Quest'][ID]
        return stored > quest_value

    def __questValue(self, ID):
        user_lvl = self.rpg_data['Level'][ID]
        entrada = self.getUserAverage(ID, 'Entrada')
        value = (10 + 1.5*user_lvl)*entrada/100
        return value

    def __userLevel(self, ID):
        level_limits = self._setLimits(self.rpg_data['Level'][ID], RPGFrame.level_pins)
        return RPGFrame.level_pins.index(level_limits[1])

