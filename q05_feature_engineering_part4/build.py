# %load q05_feature_engineering_part2/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')

def q05_feature_engineering_part4(path):
    df_shape,df = q01_load_data(path)
    df['hour'] = df['Datetime'].dt.hour
    df['month'] = df['Datetime'].dt.strftime('%b')
    df['Peakhours'] = ((df['hour']>=6) & (df['hour']<20))*1
    df['Peakmonths'] = df['month'].apply(lambda x : 1 if x in ['Feb', 'May', 'Jun', 'Jul', 'Aug'] else 0)
    return df
q05_feature_engineering_part4('data/elecdemand.csv')


