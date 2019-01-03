# %load q03_time_plot/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')
import datetime

def q03_time_plot(path):
    df_shape,df = q01_load_data(path)
    plt.plot(df['Datetime'],df['Demand'])
q03_time_plot('data/elecdemand.csv')


