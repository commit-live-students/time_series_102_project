# %load q04_boxplot/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')
import seaborn as sns

def q04_boxplot(path):
    df_shape,df = q01_load_data(path)
    sns.boxplot(x='WorkDay',y='Demand',data=df)

q04_boxplot('data/elecdemand.csv')


