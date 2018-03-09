
import pandas as pd
import numpy as np
from sklearn.model_selection import TimeSeriesSplit
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data

def q02_data_splitter(path):
    shape, data = q01_load_data(path)
    np.random.seed(9)
    'write your solution here'
    x = TimeSeriesSplit(2)
    x.random_state = 200
    splits = list(x.split(data))
    return splits    

