import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data

def q05_feature_engineering_part4(path):    
    shape, data = q01_load_data(path)
    data[['Temperature', 'Demand']].corr(method='pearson')
    data['hour'] = data['Datetime'].dt.hour
    data['month'] = data['Datetime'].dt.strftime('%b')

    'write your solution here'
    data['Peakhours'] = data['hour'].apply(lambda x: 1 if x in list(range(6, 20)) else 0)
    data['Peakmonths'] = data['month'].apply(lambda x: 1 if x in ['Feb','May', 'Jun', 'Jul', 'Aug'] else 0)
    return data


