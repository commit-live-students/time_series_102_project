# %load q02_data_splitter/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data

def q02_data_splitter(path):
    np.random.seed(9)
    df_shape,df = q01_load_data(path)
    time_series_Split = TimeSeriesSplit(n_splits=2)
    train = time_series_Split.split(X=df)
    return list(train)

q02_data_splitter('data/elecdemand.csv')


