# %load q02_data_splitter/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data

path = 'data/elecdemand.csv'

def q02_data_splitter(path):
    np.random.seed(9)
    shape,data = q01_load_data(path)
    tscv = TimeSeriesSplit(n_splits=2)
    split_data = list(tscv.split(data))
    return split_data
    
# q02_data_splitter(path)
    



