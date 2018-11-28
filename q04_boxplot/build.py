# %load q04_boxplot/build.py
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')

def q04_boxplot(path):
    
    shp,df=q01_load_data(path)
    plt.figure(figsize=(16, 7))
    sns.factorplot(x='WorkDay', y='Demand', data=df, kind='box', size=8, aspect=float(16/7))
    plt.xlabel('Workday')
    plt.ylabel('Demand')
    plt.title('Each workday demand in Australia')


