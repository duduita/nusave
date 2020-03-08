import pandas as pd
import numpy as np

def statistic_request(filter, user, data):
   '''

   :param filter:
   :param data:
   :return:
   '''

def mean_request(filter, data):
    return data[filter].mean()

def quantile15_request(filter, data):
    return data[filter].quantile(0.15)

def quantile85_request(filter, data):
    return data[filter].quantile(0.85)

def filter_resquest(filter, user, data):
    return data[user][filter]



