# %load q05_feature_engineering_part2/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data


def q05_feature_engineering_part4(path):
    shape, data = q01_load_data(path)
    data['hour'] = data['Datetime'].dt.hour
    data['month'] = data['Datetime'].dt.strftime('%b')
    data['Peakhours']=data['hour'].apply(lambda x : 1 if x in range(6,20) else 0)
    data['Peakmonths']=data['month'].apply(lambda x : 1 if x in ['Feb', 'May', 'Jun', 'Jul', 'Aug'] else 0)
    return data

#path='data/elecdemand.csv'
#q05_feature_engineering_part4(path)

