# %load q05_feature_engineering/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')

def q05_feature_engineering(path):
    path = 'data/elecdemand.csv'
    shape, df = q01_load_data(path)
    corr, p_value = pearsonr(df['Temperature'], df['Demand'])
    plt.scatter(df['Temperature'], df['Demand'])
    plt.xlabel('Temperature')
    plt.ylabel('Demand')
    plt.title('Temperature vs Demand')
    plt.show();




