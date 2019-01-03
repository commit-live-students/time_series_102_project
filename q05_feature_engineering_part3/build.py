# %load q05_feature_engineering_part3/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')

def q05_feature_engineering_part3(path):
    df_shape,df = q01_load_data(path)
    df['month'] = df['Datetime'].dt.strftime('%b')
    demands=[]
    months = ['Jan','Feb','Mar','Apr','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    for month in months:
        temp = df[df['month']==month]['Demand']
        demands.append(list(temp))
    plt.boxplot(demands,labels=months)
q05_feature_engineering_part3('data/elecdemand.csv')


