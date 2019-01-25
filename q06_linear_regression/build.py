# %load q06_linear_regression/build.py
import pandas as pd
import numpy as np
import math
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from greyatomlib.time_series_day_02_project.q05_feature_engineering_part4.build import q05_feature_engineering_part4
from greyatomlib.time_series_day_02_project.q02_data_splitter.build import q02_data_splitter

fe =  ['WorkDay', 'Peakhours', 'Peakmonths']

def q06_linear_regression(path, columns = fe, random_state = 9):
    np.random.seed(random_state)
    data = q05_feature_engineering_part4(path)
    com_idx =  q02_data_splitter(path)
    rmse = []
    for i in com_idx:
        train_idx = i[0]
        valid_idx = i[1]
        X_train, y_train = data.ix[train_idx, fe], data.ix[train_idx, 'Demand']
        X_valid, y_valid = data.ix[valid_idx, fe], data.ix[valid_idx, 'Demand']
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_valid)
        rms = mean_squared_error(y_valid, y_pred)**0.5
        rmse.append(rms)
    return np.mean(rmse)


