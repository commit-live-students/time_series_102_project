# %load q02_data_splitter/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data

def q02_data_splitter(path):
    path = 'data/elecdemand.csv'
    shape, df = q01_load_data(path)
    tscv = TimeSeriesSplit(n_splits=2)
    com_idx = []
    for train_index, valid_index in tscv.split(df):
        com_idx.append((train_index, valid_index))
    return com_idx




