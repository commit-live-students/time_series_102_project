# %load q01_load_data/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

path ='data/elecdemand.csv'

def q01_load_data(path):
    data=pd.read_csv(path)
    data['Datetime']=pd.to_datetime(data['Datetime'])
    return data.shape, data

# q01_load_data(path)


