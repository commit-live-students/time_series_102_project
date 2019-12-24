# %load q01_load_data/build.py
import pandas as pd
import numpy as np

path = 'data/elecdemand.csv'

def q01_load_data(path):
    data = pd.read_csv(path)
    data['Datetime'] = pd.to_datetime(data['Datetime'])
    return data.shape, data




