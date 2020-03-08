import pandas as pd
import numpy as np


def get_mean(filter, mes, data):
    data_mes = data[data['Mes'] == mes]
    return data_mes[filter].mean()


def get_quantile_85(filter, mes, data):
    data_mes = data[data['Mes'] == mes]
    return data_mes[filter].quantile(85)


def get_quantile(filter, mes, data):
    data_mes = data[data['Mes'] == mes]
    return data_mes[filter].quantile(85)


def get_expend(filter, user, mes, data):
    data_mes = data[data['Mes'] == mes]
    return data_mes[user][filter]

