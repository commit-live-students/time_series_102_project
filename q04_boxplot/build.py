# %load q04_boxplot/build.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from greyatomlib.time_series_day_02_project.q01_load_data.build import q01_load_data
plt.switch_backend('agg')

def q04_boxplot(path):
    path = 'data/elecdemand.csv'
    shape, df = q01_load_data(path)
    df.boxplot(column=['Demand'], by=['WorkDay'])
    plt.show();




