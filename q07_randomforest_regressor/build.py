# %load q07_randomforest_regressor/build.py
import pandas as pd
import numpy as np
import math
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from greyatomlib.time_series_day_02_project.q05_feature_engineering_part4.build import q05_feature_engineering_part4
from greyatomlib.time_series_day_02_project.q02_data_splitter.build import q02_data_splitter

fe =  ['WorkDay', 'Peakhours', 'Peakmonths']
path = 'data/elecdemand.csv'

def q07_randomforest_regressor(path,columns = fe, random_state =9):
    np.random.seed(random_state)
    data = q05_feature_engineering_part4(path)
    splits = q02_data_splitter(path)
    'write your solution here'
    
    rmse = []
    for i in splits:
        train = i[0]
        valid = i[1]
        x_train, y_train = data[fe].values[train], data['Demand'].values[train]
        x_valid, y_valid = data[fe].values[valid], data['Demand'].values[valid]
        model = RandomForestRegressor(n_estimators=50,min_samples_leaf=30,random_state=10)
        model.fit(x_train, y_train)
        pred = model.predict(x_valid)
        measure = math.pow(mean_squared_error(y_valid, pred), 0.5)
        rmse.append(measure)
    return np.mean(rmse)


