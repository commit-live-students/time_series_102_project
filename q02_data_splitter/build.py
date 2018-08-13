# %load q02_data_splitter/build.py
import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data

def q02_data_splitter(path):
    seed=9
    shape,df = q01_load_data(path)
    tssf= TimeSeriesSplit(n_splits=3)
    trainl=()
    validl=()
    for train_index,valid_index in tssf.split(df):
        trainl=trainl+ tuple(train_index)
        validl=validl + tuple(valid_index)
    return [[trainl,trainl],[validl,validl]]



