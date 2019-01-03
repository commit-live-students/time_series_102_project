# %load q05_feature_engineering/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')

def q05_feature_engineering(path):
    df_shape,df = q01_load_data(path)
    plt.scatter(df['Temperature'],df['Demand'])

q05_feature_engineering('data/elecdemand.csv')


