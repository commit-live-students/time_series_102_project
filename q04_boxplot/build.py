# %load q04_boxplot/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')

path='data/elecdemand.csv'

def q04_boxplot(path):
    shape,data = q01_load_data(path)
    data.head()
    plt.figure(figsize=(16,7))
    sns.factorplot(x='WorkDay', y='Demand', data=data, kind='box', size=8, aspect=float(16/7))
    plt.xlabel('Workday')
    plt.ylabel('Demand')
    plt.title('Change in Electricity Demand wrt to Demand')
    plt.show()
    
# q04_boxplot(path)


