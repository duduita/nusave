import random as rd
import pandas as pd

def random(x):
    return rd.uniform(0,10000)

def random_generator(dataframe, list):
    '''

    :param dataframe:
    :param list:
    :return:
    '''
    for column in list:
        dataframe[column] = dataframe['Classe'].apply(random)
    return dataframe
